import yfinance as yf
from datetime import datetime
from .models import StockRequest, StockPrice, StockResponse

class StockAgent:
    def __init__(self):
        # Dictionary to map market to symbol suffix
        self.market_suffixes = {
            "NSE": ".NS",
            "BSE": ".BO",
            "US": ""
        }

    def get_stock_price(self, request: StockRequest) -> StockResponse:
        try:
            # Format symbol based on market
            symbol = request.symbol
            
            # If it's an Indian market and suffix is not already present
            if request.market.upper() in ["NSE", "BSE"]:
                suffix = self.market_suffixes[request.market.upper()]
                if not symbol.endswith(suffix):
                    symbol = f"{symbol}{suffix}"
            
            # Get stock data using yfinance
            stock = yf.Ticker(symbol)
            info = stock.info
            
            # Get the latest price data
            history = stock.history(period=request.period)
            if history.empty:
                return StockResponse(
                    success=False,
                    message=f"No data found for symbol {symbol}"
                )
            
            latest_data = history.iloc[-1]
            
            # Convert to INR if it's an Indian stock
            currency_symbol = "₹" if request.market.upper() in ["NSE", "BSE"] else "$"
            
            stock_price = StockPrice(
                symbol=symbol,
                current_price=latest_data['Close'],
                previous_close=info.get('previousClose', 0.0),
                open_price=latest_data['Open'],
                high=latest_data['High'],
                low=latest_data['Low'],
                timestamp=latest_data.name
            )
            
            return StockResponse(
                success=True,
                message=f"Stock price retrieved successfully (Currency: {currency_symbol})",
                data=stock_price
            )
            
        except Exception as e:
            return StockResponse(
                success=False,
                message=f"Error fetching stock price: {str(e)}"
            ) 