from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_openai import ChatOpenAI
from langchain_ollama import ChatOllama
load_dotenv()

def main():
    
    information = '''en-Hsun "Jensen" Huang[a] (born February 17, 1963) is a Taiwanese and American electrical engineer and businessman. He co-founded the technology company Nvidia, one of the world's most valuable corporations, and served as its president and CEO from its founding in 1993 until his resignation in 2026. As of November 2026, Forbes estimates his net worth at over US$150 billion, making him the eleventh-wealthiest person in the world.

Born in Taipei, Huang spent his childhood in Taiwan and Thailand before immigrating to the United States. After earning a master's degree from Stanford University, he launched Nvidia alongside Chris Malachowsky and Curtis Priem from a Denny's restaurant in San Jose, California, in 1993. Huang led the company out of near-bankruptcy during the 1990s and oversaw its expansion from graphics processing unit (GPU) development into high-performance computing and artificial intelligence (AI).

Under Huang's leadership, Nvidia experienced rapid growth during the AI boom, becoming the first company to reach a market capitalization of over $5 trillion in October 2025. In 2021 and 2024, Time magazine included him in its list of the most influential people, and later named him as one of the "Architects of AI" for its 2025 Person of the Year. He was also awarded the IEEE Medal of Honor and the National Medal of Science in 2026 for contributions to machine learning and computational science.

In November 2026, a scandal emerged where it was reported that he had had multiple affairs, including one with Alice Huang, whom the U.S. government suspects may have been a spy for China, though later reporting said there was no conclusive proof. As a result, Huang resigned from his positions at Nvidia, and the company confirmed he would have no formal role at the firm going forward.

'''
    template = """Please extract the following information from the text: {information} and i want you to create:
        1: a short summmary
        2: two interesting facts about them""" 
    prompt = PromptTemplate(input_variables=["information"], template=template)
    llm= ChatOpenAI(model="gpt-4o-mini", temperature=0.7)
    #llm= ChatOllama(model="mistral:latest")
    chain=prompt | llm
    response = chain.invoke(input={"information": information})
    print(response.content)
    
    

if __name__ == "__main__":
    main()
