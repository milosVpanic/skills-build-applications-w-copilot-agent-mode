INSTALLED_APPS = [
    # ...existing apps...
    'octofit_tracker',  # Consolidate into octofit_tracker
    'corsheaders',
]

DATABASES = {
    'default': {
        'ENGINE': 'djongo',  # Add djongo as the database engine
        'NAME': 'octofit_db',
        'HOST': 'localhost',  # Explicitly set to localhost
        'PORT': 27017,
    }
}

# Enable CORS
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]
CORS_ALLOW_ALL_ORIGINS = True
CORS_ALLOW_METHODS = [
    'GET',
    'POST',
    'PUT',
    'PATCH',
    'DELETE',
    'OPTIONS',
]
CORS_ALLOW_HEADERS = [
    'content-type',
    'authorization',
    'x-csrftoken',
]

# Allow all hosts
ALLOWED_HOSTS = ['*']