#pip install phidata                         #### Framework
#pip install google-generativeai             #### For Gemini 2.0 Flash
#pip install tavily-python                   #### For Tools Integration
#pip install streamlit                       #### Entire Multi-modal agent workflow building


#from PIL import Image
from phi.agent import Agent
from phi.model.google import Gemini         #### needs an API key
from phi.tools.tavily import TavilyTools    #### also needs an API key
from constants import SYSTEM_PROMPT, INSTRUCTIONS
from dotenv import load_dotenv
load_dotenv()

##os.environ['TAVILY_API_KEY'] = st.secrets["TAVILY_API_KEY"]
##os.environ['GOOGLE_API_KEY'] = st.secrets["GOOGLE_API_KEY"]


agent = Agent(
    model = Gemini(id="gemini-2.0-flash-exp"),
    tools = [TavilyTools()],
    markdown = True,
    system_prompt = SYSTEM_PROMPT,
    instructions = INSTRUCTIONS
)

### two steps to get image:
#  first approach - file_path 

#agent.print_response( "Analyse the product image", images = ["images/bournvita.jpg"], stream = True )

#  second approach - image URL
agent.print_response( 
                    "Analysing the product image", 
                    images = ["https://external-content.duckduckgo.com/iu/?u=https%3A%2F%2Ftse4.mm.bing.net%2Fth%3Fid%3DOIP.tySLMFAgKBNNbHwxqPbZJwHaHa%26pid%3DApi&f=1&ipt=4d612fd7842215238735d04c8891234435d31e7b1a05c958399015049c9d3c6b&ipo=images"],
                    stream = True )