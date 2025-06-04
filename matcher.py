import langchain

from langchain.prompts import PromptTemplate
from langchain_community.chat_models import ChatOpenAI
from langchain.chains import LLMChain
from dotenv import load_dotenv
load_dotenv()





def get_match_analysis(resume_text , jd_text):
    with open("promts/match_promt.txt","r") as f: #reading the promt template txt
        template = f.read()

    prompt = PromptTemplate(
        input_variables=["resume","jd"], #creating a promt template object
        template = template
    )    

    llm = ChatOpenAI(   #connect to llm using lang chain
        model_name = "gpt-4o",
        temperature = 0.2)
    
    chain = LLMChain(llm=llm , prompt=prompt) #links everything into a chain

    result = chain.run({
        "resume" : resume_text ,
        "jd" : jd_text
    })
    return result
