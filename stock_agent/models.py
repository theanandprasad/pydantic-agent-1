from pydantic import BaseModel, Field
from typing import Optional, List, Literal
from datetime import datetime

class StockRequest(BaseModel):
    """Model for stock price requests"""
    symbol: str = Field(..., description="Stock symbol (e.g., AAPL, GOOGL, RELIANCE.NS, TCS.NS)")
    market: str = Field(default="US", description="Stock market (US/NSE/BSE)")
    period: str = Field(default="1d", description="Time period for stock data (1d, 5d, 1mo, etc.)")

class StockPrice(BaseModel):
    """Model for stock price data"""
    symbol: str
    current_price: float
    previous_close: float
    open_price: float
    high: float
    low: float
    timestamp: datetime

class StockResponse(BaseModel):
    """Model for stock price response"""
    success: bool
    message: str
    data: Optional[StockPrice] = None 