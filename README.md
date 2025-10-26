# dj-react

A full-stack web application built with **Django** backend and **React + TypeScript + Vite** frontend, styled with **TailwindCSS**.

## 🏗️ Project Structure

```
dj-react/
├── backend/          # Django backend
│   ├── config/       # Django project settings
│   ├── api/          # Django REST API app
│   ├── manage.py     # Django management script
│   └── requirements.txt
└── frontend/         # React + TypeScript + Vite frontend
    ├── src/          # Source files
    ├── public/       # Static files
    ├── package.json
    └── vite.config.ts
```

## 🚀 Tech Stack

### Backend
- **Django 5.2.7** - Python web framework
- **Django REST Framework 3.16.1** - API development
- **django-cors-headers 4.9.0** - CORS configuration

### Frontend
- **React 19** - UI library
- **TypeScript** - Type-safe JavaScript
- **Vite** - Fast build tool
- **TailwindCSS** - Utility-first CSS framework

## 📋 Prerequisites

- Python 3.12+
- Node.js 20+
- npm 10+

## 🛠️ Setup Instructions

### Backend Setup

1. Navigate to the backend directory:
   ```bash
   cd backend
   ```

2. Create and activate a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Run database migrations:
   ```bash
   python manage.py migrate
   ```

5. Start the Django development server:
   ```bash
   python manage.py runserver
   ```

The backend will be available at `http://127.0.0.1:8000/`

### Frontend Setup

1. Navigate to the frontend directory:
   ```bash
   cd frontend
   ```

2. Install dependencies:
   ```bash
   npm install
   ```

3. Start the Vite development server:
   ```bash
   npm run dev
   ```

The frontend will be available at `http://localhost:5173/`

## 🔌 API Endpoints

- `GET /api/hello/` - Sample endpoint that returns greeting and stack information
- `GET /api/health/` - Health check endpoint

## 🌐 CORS Configuration

The backend is configured to allow requests from:
- `http://localhost:5173` (Vite default port)
- `http://127.0.0.1:5173`

## 🎨 Features

- **Clean Architecture**: Separate backend and frontend folders
- **Type Safety**: TypeScript for frontend development
- **Modern Styling**: TailwindCSS for responsive design
- **API Communication**: Frontend fetches data from Django REST API
- **CORS Enabled**: Configured for seamless frontend-backend communication
- **Development Ready**: Hot reload for both frontend and backend

## 🔒 Security Notes

**Important**: This setup is configured for development purposes. For production deployment:

1. **SECRET_KEY**: Move the Django secret key to an environment variable
   ```python
   SECRET_KEY = os.environ.get('SECRET_KEY')
   ```

2. **DEBUG**: Set `DEBUG = False` in production

3. **ALLOWED_HOSTS**: Configure properly for your domain
   ```python
   ALLOWED_HOSTS = ['yourdomain.com', 'www.yourdomain.com']
   ```

4. **API Permissions**: Replace `AllowAny` with appropriate authentication and permission classes

5. **CORS**: Update `CORS_ALLOWED_ORIGINS` to include only your production frontend URL

6. **Database**: Use a production database (PostgreSQL, MySQL) instead of SQLite

## 🧪 Development

### Backend Development
```bash
cd backend
source venv/bin/activate
python manage.py runserver
```

### Frontend Development
```bash
cd frontend
npm run dev
```

## 📝 License

This project is open source and available under the MIT License.
