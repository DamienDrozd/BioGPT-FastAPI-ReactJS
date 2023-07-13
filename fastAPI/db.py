import motor.motor_asyncio


client = motor.motor_asyncio.AsyncIOMotorClient(
    "mongodb+srv://dems:hKifZOTwsNT33nFC@cluster0.lgyxiwj.mongodb.net/?retryWrites=true&w=majority")
db = client.sentence
