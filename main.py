from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser

# 1. Initialize the LLM
llm = ChatOpenAI(model_name="gpt-4o", temperature=0.7, openai_api_key="YOUR_API_KEY")
output_parser = StrOutputParser()

# 2. Define English Prompt Templates for each State

prompt_market = PromptTemplate.from_template(
    "Goal: {goal}\nAs a market analyst, analyze the coffee culture, high-traffic areas, and customer preferences in Baku city."
)

prompt_competitors = PromptTemplate.from_template(
    "Based on this market analysis:\n{market_analysis}\nIdentify the main competitors (both coffee chains and local cafes) in Baku, and outline their strengths and weaknesses."
)

prompt_costs = PromptTemplate.from_template(
    "Given the market conditions in Baku:\n{market_analysis}\nProvide an estimated list of setup costs including rent, equipment, licenses, and operations in AZN or USD."
)

prompt_revenue = PromptTemplate.from_template(
    "Based on the market analysis {market_analysis} and cost estimation {cost_estimate}, project a realistic revenue model and monthly profit forecast."
)

prompt_risks = PromptTemplate.from_template(
    "For the goal: {goal}, what are the key legal, economic, and cultural risks involved in opening a business in Azerbaijan (Baku)?"
)

prompt_business_plan = PromptTemplate.from_template(
    """Using all the compiled data below, generate a comprehensive and professional business plan for launching this cafe in Baku:
    Market Analysis: {market_analysis}
    Competitor Analysis: {competitor_analysis}
    Cost Estimation: {cost_estimate}
    Revenue Forecast: {revenue_forecast}
    Risk Analysis: {risk_analysis}
    """
)

# 3. Multi-State Execution using the .invoke() method

def run_multi_state_reasoning(initial_goal):
    print("🚀 Starting Multi-State Reasoning process...")
    
    # State 1: Market Analysis
    chain_market = prompt_market | llm | output_parser
    market_res = chain_market.invoke({"goal": initial_goal})
    print("✅ Step 1: Market Analysis completed.")
    
    # State 2: Competitor Analysis
    chain_competitors = prompt_competitors | llm | output_parser
    competitors_res = chain_competitors.invoke({"market_analysis": market_res})
    print("✅ Step 2: Competitor Analysis completed.")
    
    # State 3: Cost Estimation
    chain_costs = prompt_costs | llm | output_parser
    costs_res = chain_costs.invoke({"market_analysis": market_res})
    print("✅ Step 3: Cost Estimation completed.")
    
    # State 4: Revenue Forecast
    chain_revenue = prompt_revenue | llm | output_parser
    revenue_res = chain_revenue.invoke({"market_analysis": market_res, "cost_estimate": costs_res})
    print("✅ Step 4: Revenue Forecast completed.")
    
    # State 5: Risk Analysis
    chain_risks = prompt_risks | llm | output_parser
    risks_res = chain_risks.invoke({"goal": initial_goal, "market_analysis": market_res})
    print("✅ Step 5: Risk Analysis completed.")
    
    # State 6: Final Business Plan Integration
    chain_final = prompt_business_plan | llm | output_parser
    final_plan = chain_final.invoke({
        "market_analysis": market_res,
        "competitor_analysis": competitors_res,
        "cost_estimate": costs_res,
        "revenue_forecast": revenue_res,
        "risk_analysis": risks_res
    })
    print("✅ Step 6: Final Business Plan generated successfully!\n")
    
    return final_plan

# Main Execution
if __name__ == "__main__":
    input_goal = "I want to open a specialty coffee shop in Baku, Azerbaijan."
    business_plan = run_multi_state_reasoning(input_goal)
    
    print("=================== FINAL BUSINESS PLAN ===================")
    print(business_plan)