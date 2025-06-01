# 🚗 PrestigeCars – Second-Hand Car Selling Website

PrestigeCars is a Django-based web application that allows users to buy and sell second-hand cars. The platform provides a clean interface for browsing, searching, and filtering car listings, while offering features like secure payments and user dashboards to enhance the overall user experience.

---

## 🔧 Features

- 🔍 **Search & Filter Cars**: Users can browse all available cars with filters like brand, model, price, and condition.
- 🧾 **Car Detail View**: View detailed information about each car including images, specifications, and seller details.
- 🔐 **User Authentication**: Sign up, log in, and manage personal profiles.
- 💳 **Payment Integration (Test Mode)**: Integrated **Razorpay** in test mode to simulate real payments.
- ✅ **Mark as Sold**: Cars are automatically marked as sold after purchase and removed from public listings.
- 📬 **Email Confirmation**: Sends a confirmation email to the buyer after a successful transaction.
- 📊 **User Dashboard**: Buyers can view their purchased cars and their order history.
- 🧠 **Admin Panel**: Manage car listings, users, and transactions through Django’s built-in admin interface.

---

## 🛠️ Tech Stack

- **Backend**: Django (Python)
- **Frontend**: HTML, CSS, Bootstrap, JavaScript
- **Database**: postgresql (for development)
- **Payment Gateway**: Razorpay (test mode)
- **Email Service**: Django's built-in email backend (console-based for dev)

---

## 📁 Project Structure

```bash
PrestigeCars/
├── cars/                # App handling listings and car logic
├── users/               # App for user registration and dashboard
├── templates/           # HTML templates (base.html, car_list.html, etc.)
├── static/              # Static files (CSS, JS, images)
├── media/               # Uploaded car images
├── manage.py
└── requirements.txt

🚀 Getting Started
1. Clone the Repository
git clone https://github.com/your-username/prestigecars.git
cd prestigecars


3. Create and Activate Virtual Environment
python -m venv env
env\Scripts\activate    # For Windows

5. Install Dependencies
pip install -r requirements.txt

7. Run Migrations
python manage.py makemigrations
python manage.py migrate

9. Create Superuser (Optional for Admin Access)t
python manage.py createsuperuser

11. Run the Development Server
python manage.py runserver

Open your browser at http://127.0.0.1:8000/
