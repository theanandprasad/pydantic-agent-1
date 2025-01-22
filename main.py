from stock_agent.models import StockRequest
from stock_agent.agent import StockAgent

def main():
    # Create the stock agent
    agent = StockAgent()
    
    print("Welcome to Stock Price Checker!")
    print("You can check prices for US and Indian stocks.")
    print("Examples:")
    print("US Stocks: AAPL, GOOGL, MSFT")
    print("Indian Stocks: RELIANCE, TCS, INFY (for NSE)")
    print("             RELIANCE.BO, TCS.BO (for BSE)\n")
    
    # Example usage
    while True:
        symbol = input("Enter stock symbol (or 'quit' to exit): ").upper()
        if symbol == 'QUIT':
            break
        
        market = input("Enter market (US/NSE/BSE) [default: US]: ").upper() or "US"
        if market not in ["US", "NSE", "BSE"]:
            print("Invalid market. Using US market.")
            market = "US"
            
        request = StockRequest(symbol=symbol, market=market)
        response = agent.get_stock_price(request)
        
        if response.success:
            price_data = response.data
            currency = "₹" if market in ["NSE", "BSE"] else "$"
            
            print("\nStock Price Information:")
            print(f"Symbol: {price_data.symbol}")
            print(f"Current Price: {currency}{price_data.current_price:.2f}")
            print(f"Previous Close: {currency}{price_data.previous_close:.2f}")
            print(f"Open: {currency}{price_data.open_price:.2f}")
            print(f"High: {currency}{price_data.high:.2f}")
            print(f"Low: {currency}{price_data.low:.2f}")
            print(f"Timestamp: {price_data.timestamp}")
        else:
            print(f"\nError: {response.message}")
        
        print("\n" + "-"*50 + "\n")

if __name__ == "__main__":
    main() 