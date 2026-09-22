
import os
from typing import List, Literal, Any

from anthropic import Anthropic
from pydantic import BaseModel, Field, ValidationError, field_validator
from dotenv import load_dotenv


# ================================================================
# 1. LOAD ENVIRONMENT VARIABLES
# ================================================================

load_dotenv()

api_key = os.environ.get("ANTHROPIC_API_KEY")

if not api_key:
    raise ValueError(
        "ANTHROPIC_API_KEY not found. "
        "Make sure it exists in your .env file."
    )

client = Anthropic(api_key=api_key)


# ================================================================
# 2. PYDANTIC SCHEMA
# ================================================================

class SingleIncidentTicket(BaseModel):
    """
    Schema for a single parsed IT support/system incident.
    """

    ticket_id: str = Field(
        description="Unique system ticket code following format INC-XXXXX"
    )

    severity: Literal[
        "LOW",
        "MEDIUM",
        "HIGH",
        "CRITICAL"
    ] = Field(
        description="Operational impact severity level."
    )

    affected_components: List[str] = Field(
        description="Microservices, databases, or infrastructure components affected."
    )

    summary_clean: str = Field(
        description="Clean and concise summary of the incident."
    )

    assigned_team: str = Field(
        description="Engineering team responsible for the incident."
    )

    @field_validator("severity", mode="before")
    @classmethod
    def normalize_severity(cls, v: Any) -> str:

        if isinstance(v, str):
            return v.upper().strip()

        return v


# ================================================================
# 3. LOCAL PYTHON TOOL
# ================================================================

def dispatch_incident_tickets(tickets: List[dict]) -> str:

    validated_tickets: List[SingleIncidentTicket] = []

    for raw_ticket in tickets:

        try:

            # Pydantic validation
            ticket_obj = SingleIncidentTicket.model_validate(
                raw_ticket
            )

            validated_tickets.append(ticket_obj)

        except ValidationError as e:

            return (
                "Data Validation Error:\n"
                f"{e.json()}"
            )

    print(
        "\n[SYSTEM CLAUDE INTERCEPT] "
        f"Successfully validated "
        f"{len(validated_tickets)} ticket(s)."
    )

    for ticket in validated_tickets:

        print(
            f" -> Routing {ticket.ticket_id} "
            f"to [{ticket.assigned_team}] division. "
            f"Urgency: {ticket.severity}"
        )

    return (
        "SUCCESS: All incidents validated "
        "and successfully dispatched."
    )


# ================================================================
# 4. MAP CLAUDE TOOL NAME TO PYTHON FUNCTION
# ================================================================

AVAILABLE_TOOLS = {
    "dispatch_incident_tickets": dispatch_incident_tickets
}


# ================================================================
# 5. ANTHROPIC TOOL DECLARATION
# ================================================================

ANTHROPIC_TOOL_DECLARATION = [

    {
        "name": "dispatch_incident_tickets",

        "description": (
            "Processes multiple system or infrastructure "
            "incident alerts and dispatches them to "
            "the appropriate engineering teams."
        ),

        "input_schema": {

            "type": "object",

            "properties": {

                "tickets": {

                    "type": "array",

                    "description": (
                        "List of structured incident "
                        "ticket objects."
                    ),

                    "items": {

                        "type": "object",

                        "properties": {

                            "ticket_id": {
                                "type": "string",
                                "description": "Format INC-XXXXX"
                            },

                            "severity": {
                                "type": "string",
                                "enum": [
                                    "LOW",
                                    "MEDIUM",
                                    "HIGH",
                                    "CRITICAL"
                                ]
                            },

                            "affected_components": {
                                "type": "array",
                                "items": {
                                    "type": "string"
                                }
                            },

                            "summary_clean": {
                                "type": "string"
                            },

                            "assigned_team": {
                                "type": "string"
                            }
                        },

                        "required": [
                            "ticket_id",
                            "severity",
                            "affected_components",
                            "summary_clean",
                            "assigned_team"
                        ]
                    }
                }
            },

            "required": [
                "tickets"
            ]
        }
    }
]


# ================================================================
# 6. SEND LOGS TO CLAUDE
# ================================================================

def process_unstructured_syslog_with_claude(
    raw_syslog: str
):

    print(
        "Sending log block payload to Claude API..."
    )

    response = client.messages.create(

        # IMPORTANT:
        # Claude 3.5 Sonnet is retired.
        # Use an active Claude model.
        model="claude-sonnet-4-6",

        max_tokens=4000,

        system=(
            "You are a senior Site Reliability Engineer "
            "triage routing agent. "
            "Extract raw anomalies into discrete incident "
            "reports. "
            "Use the dispatch_incident_tickets tool when "
            "structured incidents have been identified."
        ),

        tools=ANTHROPIC_TOOL_DECLARATION,

        tool_choice={
            "type": "auto"
        },

        messages=[

            {
                "role": "user",

                "content": (
                    "Parse these errors and route them "
                    "appropriately:\n\n"
                    f"{raw_syslog}"
                )
            }

        ]
    )


    # ============================================================
    # 7. SEPARATE TEXT AND TOOL BLOCKS
    # ============================================================

    tool_use_blocks = [
        block
        for block in response.content
        if block.type == "tool_use"
    ]

    text_blocks = [
        block
        for block in response.content
        if block.type == "text"
    ]


    # ============================================================
    # 8. PRINT CLAUDE'S TEXT RESPONSE
    # ============================================================

    if text_blocks:

        print("\n[Claude Response]")

        for text_block in text_blocks:

            print(text_block.text)


    # ============================================================
    # 9. PROCESS TOOL CALLS
    # ============================================================

    if tool_use_blocks:

        print(
            f"\nIntercepted "
            f"{len(tool_use_blocks)} "
            f"tool application request(s) from Claude."
        )

        for tool_call in tool_use_blocks:

            function_name = tool_call.name

            function_args = tool_call.input

            tool_use_id = tool_call.id


            print(
                f"\nExecuting local function target: "
                f"{function_name}"
            )

            print(
                f"Tool Call ID: {tool_use_id}"
            )


            # ====================================================
            # FIND PYTHON FUNCTION
            # ====================================================

            target_callable = AVAILABLE_TOOLS.get(
                function_name
            )


            if target_callable:

                # Execute the Python function
                execution_msg = target_callable(
                    tickets=function_args.get("tickets", [])
                )

                print(
                    f"[Execution Response]: "
                    f"{execution_msg}"
                )

            else:

                print(
                    f"Execution Aborted: "
                    f"Tool '{function_name}' "
                    f"mapping missing from runtime."
                )

    else:

        print(
            "\nNo tool invocation requested by Claude."
        )


# ================================================================
# 10. TEST DATA
# ================================================================

if __name__ == "__main__":

    raw_production_stream = """

    [22:41:10] ERROR:
    Redis cache cluster cache-redis-primary rejected
    credentials from application tier.
    Connection pool exhausted.
    Refusing incoming traffic.
    Ticket ID reference: INC-99012.
    Shift to security or databases division.

    [22:45:19] CRITICAL:
    React UI routing failure detected.
    JavaScript chunk parsing error on home
    deployment asset.
    Incident key INC-44102.

    """

    process_unstructured_syslog_with_claude(
        raw_production_stream
    )

