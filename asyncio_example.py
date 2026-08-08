# import asyncio

# async def fetch_web_data(source_name):
#     print(f"[Start] Fetching data from {source_name}...")
    
#     await asyncio.sleep(2) 
    
#     print(f"[Done] Finished downloading from {source_name}!")
#     return f"Data Pack from {source_name}"

# async def main():
#     result = await fetch_web_data("Google API")
#     print(f"Main received: {result}")

# asyncio.run(main())
import asyncio
import time

async def web_search():
    print(" Web Search started...")
    await asyncio.sleep(3) 
    print(" Web Search finished!")
    return "Search Results"

async def read_database():
    print("Database read started...")
    await asyncio.sleep(1)  
    print(" Database read finished!")
    return "User Profile Data"

async def generate_avatar():
    print(" Avatar generation started...")
    await asyncio.sleep(2) 
    print(" Avatar generation finished!")
    return "Avatar Image URL"

async def main():
    start_time = time.time()
    print("--- Starting AI Agent System ---")

   
    results = await asyncio.gather(
        web_search(),
        read_database(),
        generate_avatar()
    )

    end_time = time.time()
    total_duration = end_time - start_time
    
    print("\n--- All Tasks Complete ---")
    print(f"Collected Data: {results}")
    print(f"Total execution time: {total_duration:.2f} seconds.")


asyncio.run(main())
