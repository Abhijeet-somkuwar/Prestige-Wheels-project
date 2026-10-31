# 🚗 Prestige Wheels – Second-Hand Luxury Car Marketplace

A full-featured **Django** web application for browsing, searching and buying pre-owned luxury cars.
It includes a polished Bootstrap front end, user accounts with email flows, Razorpay checkout (test mode),
a buyer dashboard, a customised Django admin, and a first REST API endpoint built with Django REST Framework.

![Home page](docs/screenshots/home_hero.jpg)

---

## ✨ Highlights

| Feature | What it does |
| --- | --- |
| 🔍 **Search & filter** | Filter inventory by keyword, model, city, year, body style, transmission and price range |
| 🧾 **Rich car detail pages** | Multi-image gallery, CKEditor descriptions, full specification table and inquiry form |
| 🔐 **Accounts** | Register (with welcome email), login, logout, password reset by email, Google / Facebook social login via django-allauth |
| 💳 **Razorpay checkout** | Buy a car through Razorpay (test mode); orders are tracked with pending / paid status |
| ✅ **Sold-car protection** | Purchased cars are flagged `is_sold`, badged **SOLD** in listings and cannot be bought twice |
| 📬 **Email notifications** | Purchase confirmation to the buyer and contact-form messages to the site admin |
| 📊 **Buyer dashboard** | Shows the user's inquiries and purchased cars |
| 🛠 **Custom admin** | Branded admin with thumbnails, list filters, search and quick-toggle for featured / sold |
| 🔌 **REST API** | `POST /accounts/api/login/` JSON login endpoint built with Django REST Framework |

---

## 📸 Screenshots

### Home page
Hero slider with a quick search widget, featured cars, latest listings and team section.

![Home page full](docs/screenshots/home.jpg)

### Car inventory
Paginated listing with **SOLD / FOR SALE** badges, spec chips and a sidebar search.

![Car listing](docs/screenshots/cars_listing.jpg)

### Advanced search
Filter by model, location, year, body style, transmission and price.

![Search results](docs/screenshots/search_results.jpg)

### Car detail page
Image gallery, vehicle overview, features tab, full specification panel and a Buy Now call-to-action.

| Visitor (must log in to buy) | Logged-in user | Already sold |
| --- | --- | --- |
| ![Car detail](docs/screenshots/car_detail.jpg) | ![Car detail logged in](docs/screenshots/car_detail_logged_in.jpg) | ![Sold car](docs/screenshots/car_detail_sold.jpg) |

### Razorpay checkout and confirmation

| Checkout | Payment success |
| --- | --- |
| ![Checkout](docs/screenshots/payment_checkout.jpg) | ![Payment success](docs/screenshots/payment_success.jpg) |

### Accounts

| Login | Register | Password reset |
| --- | --- | --- |
| ![Login](docs/screenshots/login.jpg) | ![Register](docs/screenshots/register.jpg) | ![Password reset](docs/screenshots/password_reset.jpg) |

### User dashboard
![Dashboard](docs/screenshots/dashboard.jpg)

### Custom admin panel
Branded Django admin with car thumbnails, filters by city / model / body style and editable **Is featured** / **Is sold** flags. Orders are tracked separately.

| Cars | Orders |
| --- | --- |
| ![Admin cars](docs/screenshots/admin_cars.jpg) | ![Admin orders](docs/screenshots/admin_orders.jpg) |

### Other pages

| About | Services | Contact |
| --- | --- | --- |
| ![About](docs/screenshots/about.jpg) | ![Services](docs/screenshots/services.jpg) | ![Contact](docs/screenshots/contact.jpg) |

---

## 🛠️ Tech stack

- **Backend:** Python 3.11, Django 5.2, Django REST Framework
- **Frontend:** HTML, CSS, Bootstrap, JavaScript (responsive template)
- **Database:** PostgreSQL
- **Auth:** Django auth + django-allauth (Google, Facebook)
- **Payments:** Razorpay (test mode)
- **Email:** SMTP (Gmail App Password) for registration, password reset and purchase confirmations
- **Rich text:** django-ckeditor; multi-select features via django-multiselectfield
- **Deployment:** Gunicorn + `Procfile` + `runtime.txt` (Heroku-style)

---

## 📁 Project structure

```text
Prestige-Wheels-project/
├── accounts/        # Register, login, dashboard, password reset, REST login API
├── cars/            # Car + CarOrder models, listing, detail, search, Razorpay checkout
├── contacts/        # Car inquiry form
├── pages/           # Home, about, services, contact, Team model
├── prestigeWheels/  # Settings, root URLs, WSGI, project static files
├── templates/       # All HTML templates (base, includes, accounts, cars, pages, admin)
├── static/          # Collected static assets
├── docs/screenshots # Images used in this README
├── .env.example     # Environment variables template
├── requirements.txt
├── Procfile / runtime.txt
└── manage.py
```

---

## 🚀 Getting started

### 1. Clone and create a virtual environment

```bash
git clone https://github.com/Abhijeet-somkuwar/Prestige-Wheels-project.git
cd Prestige-Wheels-project
python -m venv env
env\Scripts\activate        # Windows
# source env/bin/activate   # macOS / Linux
pip install -r requirements.txt
```

### 2. Configure environment variables

Copy the template and fill in your own values. The `.env` file is git-ignored.

```bash
copy .env.example .env      # Windows
# cp .env.example .env      # macOS / Linux
```

| Variable | Purpose |
| --- | --- |
| `SECRET_KEY` | Django secret key |
| `DEBUG`, `ALLOWED_HOSTS` | Debug flag and comma-separated hosts |
| `DB_NAME`, `DB_USER`, `DB_PASSWORD`, `DB_HOST`, `DB_PORT` | PostgreSQL connection |
| `EMAIL_HOST_USER`, `EMAIL_HOST_PASSWORD` | Gmail address and App Password (or set `EMAIL_BACKEND` to the console backend for local dev) |
| `RAZORPAY_KEY_ID`, `RAZORPAY_KEY_SECRET` | Razorpay test keys from the Razorpay dashboard |

### 3. Create the database and run

```bash
# create a PostgreSQL database named prestige_car_db (or whatever DB_NAME you set)
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
```

Open <http://127.0.0.1:8000/>. Add cars from the admin at <http://127.0.0.1:8000/admin/>.

---

## 🔌 REST API

```http
POST /accounts/api/login/
Content-Type: application/json

{ "username": "john", "password": "secret" }
```

Returns `200` with the user profile on success or `401` with validation errors.
See [REST_API_GUIDE.md](REST_API_GUIDE.md) for examples with fetch, cURL, Postman and Python, and [api_test.html](api_test.html) for a tiny browser test page.

---

## 🧭 Roadmap

- Token / JWT authentication for the API
- Registration and car-listing API endpoints
- Razorpay payment signature verification on the success callback
- Seller accounts so users can list their own cars

---

## 👤 Author

**Abhijeet Somkuwar** – [GitHub](https://github.com/Abhijeet-somkuwar)
