from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__, template_folder='billing_system/templates')

# GLOBAL STORAGE (Simulating System Data)
invoices = []
customers= []
users = {
    'admin': ['admin123', 'admin'],
    'user': ['user123', 'user']
}

current_user = None
customer_id_counter = 1110

# -------------------------------
#  CUSTOMER CLASS (OOP)
# -------------------------------
class Customer:
    def __init__(self, name, email, contact ):
        global customer_id_counter
        customer_id_counter += 1
        self.__id = customer_id_counter
        self.__name = name
        self.__email = email
        self.__contact = contact   

    # getters (encapsulation)
    def get_id(self):
        return self.__id

    def get_name(self):
        return self.__name

    def get_email(self):
        return self.__email

    def get_contact(self):
        return self.__contact

# setters (encapsulation)
    def set_id(self, id):
        self.__id = id

    def set_name(self, name):
        self.__name = name

    def set_email(self, email):
        self.__email = email

    def set_contact(self, contact):
        self.__contact = contact


    # update method
    def update(self, name, email, contact):
        self.__name = name
        self.__email = email
        self.__contact = contact

# -------------------------------
# 🧾 INVOICE CLASS (OOP)
# -------------------------------
class Invoice:
    invoice_counter = 5000

    def __init__(self, customer):
        Invoice.invoice_counter += 1
        self.inv__id = Invoice.invoice_counter
        self.customer = customer
        self.items = []
        self.rate = 0
        self.invoice_date = "2024-05-20"
        self.status = "Unpaid"           
        self.payment_type = "Standard"

    def add_item(self, name, quantity, price, rate=0):
        total = quantity * price

        item = {
            "name": name,
            "qty": quantity,
            "price": price,
            "total": total
        }

        self.items.append(item)

        if rate:
            self.rate = rate

    def get_items(self):
        return self.items

    def get_subtotal(self):
        return sum(i["total"] for i in self.items)

    def get_rate(self):
        return self.rate

    def get_total(self):
        subtotal = self.get_subtotal()
        return subtotal + (subtotal * self.rate / 100)

    def get_inv_id(self):
        return self.inv__id

    def get_customer(self):
        return self.customer

# -------------------------------
# HOME
# -------------------------------
@app.route('/')
def home():
    return render_template("home.html")


# -------------------------------
# Module 7:LOGIN
# -------------------------------
@app.route('/login', methods=['GET', 'POST'])
def login():
    global current_user

    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        if username in users and users[username][0] == password:
            current_user = username
            if users[username][1] == 'admin':
                return redirect(url_for('admindashboard'))
            else:
                return render_template('userdashboard.html', massage=username)
        else:
            return render_template('login.html', massage='Invalid username or password')

    return render_template('login.html', massage='')

# -------------------------------
#  DASHBOARD (Module 1: Customer Management)
# -------------------------------
@app.route('/admindashboard')
def admindashboard():
    if not current_user:
        return redirect(url_for('login'))
    if users[current_user][1] != 'admin':
        return redirect(url_for('userdashboard'))
    
    search_query = request.args.get('search', '').lower()

    if search_query:
        filtered_customers = [
            c for c in customers 
            if search_query in str(c.get_id()) or search_query in c.get_name().lower()
        ]
    else:
        filtered_customers = customers

    return render_template("admindashboard.html", customers=filtered_customers, user_type='admin')

@app.route('/userdashboard')
def userdashboard():
    if not current_user:
        return redirect(url_for('login'))
    if users[current_user][1] != 'user':
        return redirect(url_for('admindashboard'))
    
    search_query = request.args.get('search', '').lower()

    if search_query:
        filtered_customers = [
            c for c in customers 
            if search_query in str(c.get_id()) or search_query in c.get_name().lower()
        ]
    else:
        filtered_customers = customers

    return render_template("userdashboard.html", customers=filtered_customers, user_type='user')


# -------------------------------
#  ADD CUSTOMER
# -------------------------------
@app.route('/add_customer', methods=['GET', 'POST'])
def add_customer():
    global current_user
    if not current_user:
        return redirect(url_for('login'))
    
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        contact = request.form['contact']

        new_customer = Customer(name, email, contact,)
        customers.append(new_customer)


        if users[current_user][1] == 'admin':
            return redirect(url_for('admindashboard'))
        elif users[current_user][1] == 'user':
            return redirect(url_for('userdashboard'))
        else:
            return redirect(url_for('add_customer'))

    return render_template("add_customer.html")


# -------------------------------
#  DELETE CUSTOMER
# -------------------------------
@app.route('/delete/<int:id>')
def delete_customer(id):
    if not current_user:
        return redirect(url_for('login'))
    if users[current_user][1] != 'admin':
        return redirect(url_for('userdashboard'))  # Only admins can delete
    
    global customers
    customers = [c for c in customers if c.get_id() != id]
    return redirect(url_for('admindashboard'))

# -------------------------------
#  EDIT CUSTOMER
# -------------------------------
@app.route('/edit/<int:id>', methods=['GET', 'POST'])
def edit_customer(id):
    
    # Find customer, handle error if not found
    customer = next((c for c in customers if c.get_id() == id), None)

    if request.method == 'POST':
        customer.update(
            request.form['name'],
            request.form['email'],
            request.form['contact']
        )
        return redirect(url_for('admindashboard'))
    
    return render_template("edit_customer.html", customer=customer)

#-----------------------------
# Module 2:INVOICE MANAGEMENT
#-----------------------------
@app.route('/invoice')
def invoice():
    if not current_user:
        return redirect(url_for('login'))
    user_type = users[current_user][1] if current_user in users else 'user'
    return render_template('invoice.html', invoices=invoices, customers=customers, user_type=user_type)

@app.route('/create_invoice/<int:customer_id>', methods=['GET', 'POST'])
def create_invoice(customer_id):
    if not current_user:
        return redirect(url_for('login'))
    user_type = users[current_user][1] if current_user in users else 'user'

    customer = next((c for c in customers if c.get_id() == customer_id), None)

    if not customer:
        return "Customer not found"

    if request.method == 'POST':
        if 'action' in request.form and request.form['action'] == 'finalize':
            # Finalize the invoice - redirect to invoice list
            return redirect(url_for('invoice'))

        name = request.form['item_name']
        quantity = int(request.form['qty'])
        price = float(request.form['price'])
        rate = request.form.get('rate')

        rate = float(rate) if rate else 0

        if 'invoice_id' not in request.form:
            invoice = Invoice(customer)
            invoice.add_item(name, quantity, price, rate)
            invoices.append(invoice)
        else:
            invoice_id = int(request.form['invoice_id'])
            invoice = next(i for i in invoices if i.get_inv_id() == invoice_id)
            invoice.add_item(name, quantity, price, rate)

        return render_template("create_invoice.html", customer=customer, invoice=invoice, user_type=user_type)

    return render_template("create_invoice.html", customer=customer, invoice=None, user_type=user_type)

# -------------------------------
# Module 4: Balance and billing tracking
#--------------------------------
@app.route('/balance')
def balance():
    if not current_user:
        return redirect(url_for('login'))
    user_type = users[current_user][1] if current_user in users else 'user'
    
    customer_balances = {}

    for cust in customers:
        customer_id = cust.get_id()
        # Initialize the dictionary for this customer
        customer_balances[customer_id] = {
            "name": cust.get_name(),
            "email": cust.get_email(),
            "contact": cust.get_contact(),
            "total_invoiced": 0.0,
            "paid": 0.0,
            "outstanding": 0.0,
            "invoices": []
        }

        # Find all invoices belonging to this customer object
        for inv in invoices:
            if inv.get_customer() == cust:
                total_amount = inv.get_total()
                
                # Create a dictionary for the template to read easily
                inv_data = {
                    "invoice_number": inv.get_inv_id(),
                    "invoice_date": inv.invoice_date,
                    "payment_type": inv.payment_type,
                    "total": total_amount,
                    "status": inv.status
                }
                
                customer_balances[customer_id]["invoices"].append(inv_data)
                customer_balances[customer_id]["total_invoiced"] += total_amount
                
                # Logic for Paid vs Outstanding
                if inv.status == "Paid":
                    customer_balances[customer_id]["paid"] += total_amount
                else:
                    customer_balances[customer_id]["outstanding"] += total_amount

    return render_template('balance.html', customer_balances=customer_balances, user_type=user_type)

#-------------------------
# Payment Management
#-------------------------
@app.route('/payment')
def payment():
    if not current_user:
        return redirect(url_for('login'))
    user_type = users[current_user][1] if current_user in users else 'user'
    
    # Prepare pending invoices for payment
    pending_invoices = []
    for inv in invoices:
        if inv.status != "Paid":
            invoice_data = {
                "id": inv.get_inv_id(),
                "customer_name": inv.get_customer().get_name(),
                "invoice_date": inv.invoice_date,
                "due_date": "2024-06-20",  # Placeholder
                "payment_type": inv.payment_type,
                "total": inv.get_total(),
                "paid_amount": 0.0,  # Placeholder - need to implement payments
                "status": inv.status,
                "payments": []  # Placeholder
            }
            # Add get_remaining_balance method result
            invoice_data["get_remaining_balance"] = lambda: invoice_data["total"] - invoice_data["paid_amount"]
            pending_invoices.append(invoice_data)
    
    return render_template('payment.html', pending_invoices=pending_invoices, user_type=user_type)

#-----------------------------
# Module 6: Report Management 
#-----------------------------
@app.route('/report')
def report():
    return render_template('report.html')

@app.route('/logout')
def logout():
    return redirect(url_for('login'))
# -------------------------------
# ▶️ RUN
# -------------------------------
if __name__ == '__main__':
    app.run(debug=True)