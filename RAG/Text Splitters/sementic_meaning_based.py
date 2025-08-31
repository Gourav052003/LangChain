from langchain_experimental.text_splitter import SemanticChunker
from langchain_openai import OpenAIEmbeddings
from dotenv import load_dotenv
load_dotenv()

text = """
Google was founded on September 4, 1998, by American computer scientists Larry Page and Sergey Brin. Together, they own about 14% of its publicly listed shares and control 56% of its stockholder voting power through super-voting stock. The company went public via an initial public offering (IPO) in 2004. The meaning of spirituality has developed and expanded over time, and various meanings can be found alongside each other.[1][2][3][note 1] Traditionally, spirituality referred to a religious process of re-formation which "aims to recover the original shape of man",[note 2] oriented at "the image of God"[4][5] as exemplified by the founders and sacred texts of the religions of the world. The term was used within early Christianity to refer to a life oriented toward the Holy Spirit[6] and broadened during the Late Middle Ages to include mental aspects of life. 

Cricket is a bat-and-ball game that is played between two teams of eleven players on a field, at the centre of which is a 22-yard (20-metre; 66-foot) pitch with a wicket at each end, each comprising two bails (small sticks) balanced on three stumps. Two players from the batting team, the striker and nonstriker, stand in front of either wicket holding bats, while one player from the fielding team, the bowler, bowls the ball toward the striker's wicket from the opposite end of the pitch.
"""

text_splitter = SemanticChunker(
    OpenAIEmbeddings(),
    breakpoint_threshold_type = "standard_deviation",
    breakpoint_threshold_amount=0.5,
)

docs = text_splitter.create_documents([text])
print(docs)
print(len(docs))