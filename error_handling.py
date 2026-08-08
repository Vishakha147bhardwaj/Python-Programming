# A list tracking departments slated for review
departments = ["Marketing_Data", "Finance_Data_Corrupted", "Sales_Data_Missing"]

for dept in departments:
    print(f"\n🎬 Reviewing pipeline channel: [{dept}]")
    
    try:
        if dept == "Marketing_Data":
            ad_spend = 5000
            clicks = 250
            cost_per_click = ad_spend / clicks
            print(f"   📈 Analytics calculated smoothly. CPC: ${cost_per_click:.2f}")
            
        elif dept == "Finance_Data_Corrupted":
            ad_spend = 1200
            clicks = 0
            # Math Warning: You cannot divide a number by zero! This causes a system crash.
            cost_per_click = ad_spend / clicks 
            
        elif dept == "Sales_Data_Missing":
            # Trying to open a spreadsheet file that doesn't actually exist on our machine.
            with open("non_existent_records.csv", "r") as sheet:
                data = sheet.read()

    # Intercept zero division calculations safely
    except ZeroDivisionError as math_error:
        print("   🚨 [ALERT] division bypass triggered. Click volume metric is missing.")
        print(f"      ↳ Details: {math_error}")
        
    # Intercept missing file paths safely
    except FileNotFoundError as file_error:
        print("   🚨 [ALERT] file bypass triggered. The targeted data sheet cannot be found.")
        print(f"      ↳ Details: {file_error}")
        
    # Run cleanup steps that must execute every single time
    finally:
        # Append progress markers to a checklist file so we know what ran
        with open("pipeline_checkpoint.txt", "a", encoding="utf-8") as audit_file:
            audit_file.write(f"Concluded pass for: {dept}\n")
        print(f"   🔒 [Security] Logged processing metadata for {dept}.")

print("\n==================================================")
print("✅ PIPELINE COMPLETED: ALL CHANNELS EVALUATED GRACEFULLY")
print("==================================================")
