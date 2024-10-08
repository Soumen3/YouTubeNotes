﻿# YouTubeNotes

YouTubeNotes is a web application that allows users to take notes on YouTube videos. This project is built using Django for the backend and TailwindCSS for styling.

## Features
- User authentication
- Note-taking on YouTube videos
- Responsive design with TailwindCSS

## Prerequisites
- Python 3.x
- Django
- Node.js (for TailwindCSS)

## Installation

1. Clone the repository:
    ```sh
    git clone https://github.com/Soumen3/YouTubeNotes.git
    cd YouTubeNotes
    ```

2. Create a virtual environment and activate it:
    ```sh
    python -m venv venv
    venv\Scripts\activate  # On Windows
    # source venv/bin/activate  # On macOS/Linux
    ```

3. Install the required Python packages:
    ```sh
    pip install -r req.txt
    ```

4. Install TailwindCSS:
    ```sh
    npm install
    ```

## Run The Servers

- Django: 
    ```sh
    python manage.py runserver
    ```

- TailwindCSS: 
    ```sh
    python manage.py tailwind start
    ```

## Usage

1. Open your browser and navigate to `http://127.0.0.1:8000/`.
2. Register for a new account or log in with an existing account.
3. Start taking notes on your favorite YouTube videos!

## Contributing

1. Fork the repository.
2. Create a new branch: `git checkout -b my-feature-branch`
3. Make your changes and commit them: `git commit -m 'Add some feature'`
4. Push to the branch: `git push origin my-feature-branch`
5. Submit a pull request.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
