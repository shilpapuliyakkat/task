a=int(input("enter quantity of product A:"))
s1=input("product is wrapped as gift yes/no:")

b=int(input("enter quantity of product B:"))
s2=input("product is wrapped as gift yes/no:")

c=int(input("enter quantity of product C:"))
s3=input("product is wrapped as gift yes/no:")
priceA=20
priceB=40
priceC=50
total_quantity=a+b+c
shipping_fee=(total_quantity/10)*5
if s1=="yes":
    wrapA=a*1
if s2=="yes":
    wrapB=b*1
if s3=="yes":
    wrapC=c*1
wrapfee=wrapA+wrapB+wrapC
total_amountA=20*a
total_amountB=40*b
total_amountC=50*c
cart_total=0
cart_total=total_amountA+total_amountB+total_amountC
subtotal=cart_total+wrapfee+shipping_fee
#print(cart_total)
flat_10_discount=0
if cart_total>200:
    flat_10_discount=(cart_total*10)/100
    #print(flat_10)
    flat_10_amount=subtotal-flat_10_discount
    #print(flat_10_discount)
bulk_5_discount=0
discount_amountA=0
discount_amountB=0
discount_amountC=0
# total_amountA=0
# total_amountB=0
# total_amountC=0
if a>10:
    discount_amountA=(total_amountA*5)/100
    total_amountA=total_amountA-discount_amountA
if b>10:
    discount_amountB=(total_amountB*5)/100
    total_amountB=total_amountB-discount_amountB
if c>10:
    discount_amountC=(total_amountC*5)/100
    total_amountC=total_amountC-discount_amountC
    bulk_5_discount=discount_amountA+discount_amountB+discount_amountC
    bulk_5_amount=total_amountA+total_amountB+total_amountC+wrapfee+shipping_fee
    #print(bulk_5_discount)

bulk_10_discount=0
if total_quantity>20:
    bulk_10_discount=(cart_total*10)/100
    #print(bulk_10)
    bulk_10_amount=subtotal-bulk_10_discount
    #print(bulk_10_discount)

tiered_50_discount=0
discountA=0
discountB=0
discountC=0
if total_quantity>30 and a>15:
   discountA=(a-15)*20*50/100
   total_amountA=15*20+discountA
if total_quantity>30 and b>15:
    discountB=(b-15)*40*50/100
    total_amountB=15*40+discountB
if total_quantity>30 and c>15:
    discountC = ((c - 15) * 50 * 50) / 100
    total_amountB = 15*50+discountC
    tiered_50_discount=discountA+discountB+discountC
    print(tiered_50_discount)
    #print(tiered_50_discount_total)
    tiered_50_amount=total_amountA+total_amountB+total_amountC+wrapfee+shipping_fee
   # print(tiered_50_discount)

def discount():
   if flat_10_discount>bulk_5_discount and flat_10_discount>bulk_10_discount and flat_10_discount>tiered_50_discount:
    print("flat_10_discount:",flat_10_discount)
    print("Total:",flat_10_amount)
   elif bulk_5_discount>flat_10_discount and bulk_5_discount>bulk_10_discount and bulk_5_discount>tiered_50_discount:
    print("bulk_5_discount:",bulk_5_discount)
    print("Total:", bulk_5_amount)
   elif bulk_10_discount>flat_10_discount and  bulk_10_discount>bulk_5_discount and bulk_10_discount>tiered_50_discount:
    print("bulk_10_discount:",bulk_10_discount)
    print("Total:", bulk_10_amount)
   else:
    print("tiered_50_discount:",tiered_50_discount)
    print("Total:", tiered_50_amount)

print("productA",a,total_amountA)
print("productB",b,total_amountB)
print("productC",c,total_amountC)
print("subtotal:",subtotal)
print("shipping fee:",shipping_fee)
print("wrapp fee:",wrapfee)
discount()

