class Product:
    def __init__(self,name,price,deal_price,rating):
        self.name=name
        self.price=price
        self.deal_price=deal_price
        self.rating=rating
        self.you_save= price - deal_price
    
    def display_product_details(self):
        print("Product: {}".format(self.name))
        print("Price: {}".format(self.price))
        print("Deal Price: {}".format(self.deal_price))
        print("Rating: {}".format(self.rating))
        print("You Save: {}".format(self.you_save))
    
    def get_deal_price(self):
        return self.deal_price
        
class Electronicproduct(Product):
    def __init__(self,name,price,deal_price,rating,warrenty_in_months):
        super().__init__(name,price,deal_price,rating)
        self.warrenty_in_months=warrenty_in_months
    
    def set_warrenty(self,warrenty_in_months):
        self.warrenty_in_months=warrenty_in_months
        
    def display_product_details(self):
        super().display_product_details()
        print("Warrenty In Months: {}".format(self.warrenty_in_months))
        
class Groceryproduct(Product):
    def __init__(self,name,price,deal_price,rating,expire_date):
        super().__init__(name,price,deal_price,rating)
        self.expire_date=expire_date
    
    def set_expire(self,expire_date):
        self.expire_date=expire_date
        
    def display_product_details(self):
        super().display_product_details()
        print("Expire Date: {}".format(self.expire_date))

class Order:
    delivery_charges={
        "Prime":0,
        "Normal":50
    }
    def __init__(self,delivery_method,delivery_address):
        self.items_in_cart=[]
        self.delivery_address=delivery_address
        self.delivery_method=delivery_method
        
    def add_item(self,product,quanity):
        self.items_in_cart.append((product,quanity))
        
    def display_cart(self):
        for product,quanity in self.items_in_cart:
            product.display_product_details()
            print("--------------------------------------")
        
        print("Delivery Method: {}".format(self.delivery_method))
        print("Delivery Address: {}".format(self.delivery_address))
        
    
    def total_price(self):
        total_price=0
        for product,quanity in self.items_in_cart:
            total_price+=product.get_deal_price()*quanity
        
        total_price=total_price+Order.delivery_charges[self.delivery_method]
        print("----------------------")
        print("Total Bill: {}".format(total_price))
        print("-----------------------")

#Adding Electronic Items
Tv=Electronicproduct("LG",10000,9000,"5 Stars","5 Years")
Keyboard=Electronicproduct("Key Board QWERTY",1000,800,"4 Stars", "1 Year")
Mouse=Electronicproduct("Wirless Mouse",500,400,"5 Stars","1 Year")

#Adding Grocery Items
Milk=Groceryproduct("Milk",30,25,"4 Stars","27-05-2021")
Wheat=Groceryproduct("Wheat Powder",45,40,"4 Stars","27-07-2021")
GroundNuts=Groceryproduct("Gorund nuts",40,38,"5 Stars","27-08-2021")

#Adding items in the car
order=Order("Normal","Rajampet")
order.add_item(Tv,1)
order.add_item(Keyboard,1)
order.add_item(Mouse,1)
order.add_item(Milk,2)
order.add_item(Wheat,3)
order.add_item(GroundNuts,12)
order.display_cart()
order.total_price()
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        