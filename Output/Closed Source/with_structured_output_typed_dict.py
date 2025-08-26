from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
from typing import TypedDict, Annotated, Optional, Literal

load_dotenv()

model = ChatOpenAI()

#schema

# class Review(TypedDict):
#     summary: str
#     sentiment: str


# class Review(TypedDict):
#     summary: Annotated[str,"A brief summary of the review"]
#     sentiment: Annotated[str,"Overall sentiment of the review, either 'positive', 'negative', or 'neutral'"]

# class Review(TypedDict):
#     key_themes: Annotated[list[str],"Key themes discussed in the review in a list"]
#     summary: Annotated[str,"A brief summary of the review"]
#     sentiment: Annotated[str,"Overall sentiment of the review, either 'positive', 'negative', or 'neutral'"]
#     pros: Annotated[Optional[list[str]],"List of pros mentioned in the review, if any"]
#     cons: Annotated[Optional[list[str]],"List of cons mentioned in the review, if any"]

class Review(TypedDict):
    key_themes: Annotated[list[str],"Key themes discussed in the review in a list"]
    summary: Annotated[str,"A brief summary of the review"]
    sentiment: Annotated[Literal["pos","neg"],"Overall sentiment of the review, either 'positive', 'negative', or 'neutral'"]
    pros: Annotated[Optional[list[str]],"List of pros mentioned in the review, if any"]
    cons: Annotated[Optional[list[str]],"List of cons mentioned in the review, if any"]

structured_model = model.with_structured_output(Review)

# result = structured_model.invoke("""Absolutely love this phone! The display is bright and crisp, battery easily lasts more than a day, and the camera quality is stunning even in low light""")


#review with pros and cons
# result = structured_model.invoke("""I've been using this smartphone for a little over a month, and it's been a mostly positive experience. The display is one of the first things you notice—bright, colorful, and super smooth thanks to the high refresh rate. Watching videos or just scrolling through apps feels really fluid. Performance has been excellent too. Apps open instantly, games run without lag, and switching between tasks is seamless. The camera is another highlight; photos are sharp, colors look natural, and low-light shots are surprisingly detailed. The battery life is solid as well—on a full charge it lasts me an entire day of heavy use, and charging it up is quick enough that I never feel stuck waiting around. The overall design also feels premium, slim, and comfortable to hold, which adds to the appeal.

# That said, it's not perfect. The price is definitely on the higher side, and it stings when you realize there's no headphone jack or option to expand storage with a memory card. While the fingerprint sensor works most of the time, it's a little finicky and slower than I'd like. I've also noticed that the phone tends to heat up during long gaming sessions or extended camera use, which is a bit disappointing in such an expensive device.

# Overall, though, I'm happy with the purchase. It delivers fantastic performance, a stunning screen, and one of the best camera experiences out there. If you're willing to pay a premium and don't mind a few small trade-offs, it's a great choice.""")

# review without cons
result = structured_model.invoke("""This smartphone has completely exceeded my expectations. The display is absolutely stunning—colors are vivid, blacks are deep, and the smooth refresh rate makes every interaction feel effortless. Watching movies, gaming, or just browsing social media feels like a premium experience.

Performance is lightning fast thanks to the latest processor. Apps launch instantly, multitasking is seamless, and even heavy games run without any stutter. The camera system is another standout feature. Photos come out crystal clear with vibrant colors, and the night mode captures detail that rivals professional cameras. Videos are equally impressive with excellent stabilization.

The battery life is more than enough for a full day of heavy use, and the fast charging is a game changer. In less than half an hour, the phone charges up to a level where I can comfortably get through the rest of the day. The design is sleek and elegant, with a premium feel that's both stylish and comfortable to hold.

The software experience is clean and intuitive, with useful features that enhance day-to-day use without cluttering the phone. Regular updates give me peace of mind about security and future performance.

Overall, this is one of the best smartphones I've ever used. It strikes the perfect balance between design, performance, and camera quality, making it a device I truly enjoy using every single day.""")


print(result)
# print(result['cons']) # will give error if cons is not present in the result
print(type(result))



