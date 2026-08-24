import json
import datetime
import random

random.seed(42)

products = [
    (PRD-101, MacBook Pro M3 Max 16-inch, Electronics, 319900, 1),
    (PRD-102, Enterprise AI Cloud Subscription Annual, SaaS Software, 185000, 1),
    (PRD-103, Ergonomic Herman Miller Chair, Furniture, 84500, 2),
    (PRD-104, Dell UltraSharp 32-inch 4K USB-C Monitor, Electronics, 68900, 3),
    (PRD-105, SalesPulse CRM Enterprise License, SaaS Software, 49999, 1),
    (PRD-106, Standing Electric Desk Pro, Furniture, 42000, 2),
    (PRD-107, Sony WH-1000XM5 Wireless Headphones, Audio, 29990, 5),
    (PRD-108, Logitech MX Master 3S Mechanical Combo, Accessories, 18990, 8),
    (PRD-109, Anker PowerStation 100W Fast Charger, Accessories, 8499, 12),
    (PRD-110, Bose SoundLink Revolve II Speaker, Audio, 24500, 4),
    (PRD-111, Data Analytics Pipeline Connector Pro, SaaS Software, 75000, 2),
    (PRD-112, Apple iPad Air M2 256GB, Electronics, 69900, 3),
]

customers = [
    (Reliance Retail Ltd, procurement@reliance.in, Mumbai, West),
    (Tata Consultancy Services, infra.buy@tcs.com, Mumbai, West),
    (Infosys Digital Labs, vendor@infosys.com, Bengaluru, South),
    (HDFC Financial Services, it.assets@hdfcbank.com, Mumbai, West),
    (Wipro Technologies, tech.orders@wipro.com, Bengaluru, South),
    (Aarav Sharma, aarav.s@gmail.com, Delhi, North),
    (Priya Patel Enterprises, priya@pateldesign.co, Ahmedabad, West),
    (Vikram Malhotra, vikram.m@techstart.io, Gurugram, North),
    (Ananya Iyer, ananya.iyer@creativestudio.in, Chennai, South),
    (Zomato Media Pvt Ltd, infra@zomato.com, Gurugram, North),
    (Razorpay Tech Labs, hardware@razorpay.com, Bengaluru, South),
    (Apollo Health Logistics, supply@apollohealth.org, Hyderabad, South),
    (Kolkata Port Logistics, ops@kplogistics.in, Kolkata, East),
    (Bhubaneswar Softworks, contact@bbsrsoft.com, Bhubaneswar, East),
    (Naveen Gupta, naveen.gupta@consultant.in, Noida, North),
    (Deepika Sen, deepika.sen@designhub.in, Kolkata, East),
]

salespersons = [Rahul Verma, Ananya Sen, Kavita Rao, Deepak Nair, Rohan Mehta]
payment_methods = [UPI, Credit Card, Net Banking, Debit Card, Bank Transfer]
statuses = [completed, completed, completed, completed, pending, completed, refunded, cancelled]

records = []
base_date = datetime.date(2026, 8, 20)

for i in range(1, 145):
    days_ago = int((i ** 1.1) % 115)
    order_date = base_date - datetime.timedelta(days=days_ago)
    
    prod = random.choice(products)
    cust = random.choice(customers)
    salesperson = random.choice(salespersons)
    pay_method = random.choice(payment_methods)
    status = random.choice(statuses)
    
    qty = random.randint(1, prod[4])
    unit_price = prod[3]
    discount = 0
    if random.random() < 0.25:
        discount = int(unit_price * qty * random.choice([0.05, 0.10, 0.15]))
    
    amount = (unit_price * qty) - discount
    order_id = fORD-2026-{1000 + i}
    time_str = f{random.randint(9, 20):02d}:{random.randint(0, 59):02d}:{random.randint(0, 59):02d}
    iso_date = f{order_date.isoformat()}T{time_str}Z
    
    records.append({
        id: i,
        order_id: order_id,
        date: iso_date,
        amount: amount,
        customer_name: cust[0],
        customer_email: cust[1],
        customer_city: cust[2],
        region: cust[3],
        product_id: prod[0],
        product_name: prod[1],
        category: prod[2],
        quantity: qty,
        unit_price: unit_price,
        discount: discount,
        salesperson: salesperson,
        payment_method: pay_method,
        status: status,
        notes: fCommercial transaction via {pay_method}
    })

records.sort(key=lambda r: r[date], reverse=True)

ts_content = import { SaleRecord } from '@/types/sales';\n\nexport const SAMPLE_SALES_RECORDS: SaleRecord[] =  + json.dumps(records, indent=2) + ;\n

with open(rC:\Users\harsh\.gemini\antigravity\scratch\sales-dashboard\src\utils\sampleData.ts, w, encoding=utf-8) as f:
    f.write(ts_content)

print(fGenerated {len(records)} sample sales records.)
