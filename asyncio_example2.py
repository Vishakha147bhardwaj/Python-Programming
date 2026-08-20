import asyncio
import time

# Define an async task
async def brew_coffee(cup_number):
    print(f"☕ Start brewing coffee cup #{cup_number}...")
    # Simulate waiting for the machine to drip (takes 2 seconds)
    # we use asyncio.sleep instead of time.sleep because it allows pausing
    await asyncio.sleep(2) 
    print(f"✅ Coffee cup #{cup_number} is ready!")

async def main():
    start_time = time.time()
    
    # Run 3 coffee brewing tasks simultaneously
    await asyncio.gather(
        brew_coffee(1),
        brew_coffee(2),
        brew_coffee(3)
    )
    
    end_time = time.time()
    print(f"Total time taken: {end_time - start_time:.2f} seconds")

# Run the async program management loop
asyncio.run(main())
