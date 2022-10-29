# stockdatascraper

Stock Data Scraper by Neel Dhall

Access the following data of any public equity at ease via US ticker:
- Operating Margin
- ROI
- EBITDA
- Price to Book
- Price to Earnings
- Dividend Yield
- Free Cash Flow Yield
- Debt to Equity Ratio
- Current Ratio

How data is scored:

Return on investment (ROI)
20+% over 5 years - 10 
18-20 % over 5 years - 9 
16-18 % over 5 years - 8
14-16 % over 5 years - 7 
12-14 % over 5 years - 6 
10-12 % over 5 years - 5 
8-10 % over 5 years - 4 
6-8 % over 5 years - 3 
4-6 % over 5 years - 2
<0-4 % over 5 years - 1

Operating Proft Margin = Operating proft/net sales *100
27+% over 5 years - 10
24-27+% over 5 years - 9
22-24% over 5 years - 8
20-22% over 5 years - 7 
16-20% over 5 years - 6 
13-16% over 5 years - 5 
10-13% over 5 years - 4
5-10 % over 5 years - 3
0-5% over 5 years - 2 
<0% over 5 years - 1

Free Cash Flow Yield (FCF Yield) 
14+% - 10 
11-14% - 9 
9-12% - 8
7-9% - 7 
5-7% - 6 
4-5% - 5 
2-4% - 4
1-2% - 3
0-1% - 2
<0% - 1 

EBITDA (Earnings Before Interest, Taxes, Depreciation and Amortization) 
Varies heavily by industry
29%+ - 10 
26-29% - 9
23-26% - 8
20 - 23% - 7
17 - 20% - 6 
14- 17% - 5
11 - 14% - 4 
8 - 11% - 3 
5 - 8% - 2
<5% - 1

Dividend Yield 
5.75%+ - 10
4.75 - 5.75% - 9 
4 - 4.75% - 8
3.25 - 4 % - 7
2.5 - 3.25% - 6 
1.75 - 2.5% - 5
1 - 1.75% - 4 
0. 5 - 1% - 3 
0.1 - 0.5% - 2
NA - 1 

P/E (Price to Earnings) → 10 is most undervalued/1 is most overvalued 
<3 - 10
3-8 - 9
8-12 - 8
12-15 - 7
15-20 - 6
20-30 - 5
30-45 - 4 
45-60 - 3
60-80 -2 
80+ - 1 

P/B (Price to Book) → 10 is most undervalued/1 is most overvalued 
if <1 - 10 
1 - 1.5 - 9 
1.5 - 2.0 - 8 
2.0 - 2.5 - 7
2.5 - 3.0 - 6
3.0 - 3.5 - 5
3.5 - 4.0 - 4
4.0 - 4.5 - 3 
4.5 - 5.0 - 2
if >5.0 - 1

Current Ratio 
if >8 - 10 
6-8 - 9
4-6 - 8 
2.5 -4 - 7 
1.75 - 2.5 - 6
1.25-1.75 -5 
1.25-1.00 - 4
1.00-0.75 - 3
0.75-0.50 - 2 
if >0.5 - 1

Debt to Equity 
if <0.5-10
0.8-0.5 - 9
1.0-0..8 - 8
1.2-1.0 - 7
1.4-1.2 - 6
1.8-1.4 - 5
2.5-1.8 - 4
3.2 - 2.5 - 3
4.0-3.2 - 2
if >4-1
