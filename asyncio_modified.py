import asyncio
import time

# Simulate an external network fetch operation
async def fetch_api_data(service_name, delay):
    print(f"[Start] Fetching from {service_name}...")
    # asyncio.sleep mimics an I/O network pause without freezing execution
    await asyncio.sleep(delay) 
    print(f"[Done] Finished fetching {service_name}.")
    return f"{service_name} Data"

async def main():
    start_time = time.time()
    
    # Bundle tasks to run simultaneously using asyncio.gather
    results = await asyncio.gather(
        fetch_api_data("PaymentGateway", 2),
        fetch_api_data("UserProfileDB", 3),
        fetch_api_data("InventoryCheck", 1)
    )
    
    print(f"\nAll data retrieved successfully: {results}")
    end_time = time.time()
    # Traditional sequential code takes 6 seconds (2 + 3 + 1)
    # Async takes only about 3 seconds (the duration of the longest task)
    print(f"Total processing time: {end_time - start_time:.2f} seconds")

# Fire up the event loop to drive the main execution routine
asyncio.run(main())
