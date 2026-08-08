import asyncio
import time

# Define a single task capable of pausing
async def fetch_report(report_name, wait_time):
    print(f"🔄 Requesting '{report_name}' from the cloud server...")
    # Simulate waiting for a slow server download without freezing Python
    await asyncio.sleep(wait_time)
    print(f"✅ '{report_name}' download complete!")

# Define the master coordinator function
async def main():
    start_time = time.time()
    print(start_time)
    
    # Bundle up three separate slow network requests to run concurrently
    await asyncio.gather(
        fetch_report("Google Ads Data", 3),
        fetch_report("SEO Positions Report", 2),
        fetch_report("Email Click Metrics", 1)
    )
    
    end_time = time.time()
    print(end_time)
    print(f"\n⏱️ Total time taken to fetch all reports: {end_time - start_time:.1f} seconds")

# Tell the master head chef to run our code pipeline
asyncio.run(main())
