# Yaproq Bot
#### Yaproq botni [usbu link orqali kirib](https://t.me/yaproq1bot) ko'rib ishlatib ko'rishingiz mumkin
#

<!-- GETTING STARTED -->
## Getting Started

This is an example of how you may give instructions on setting up your project locally.
To get a local copy up and running follow these simple example steps.

### Prerequisites

This is an example of how to list things you need to use the software and how to install them.


### Installation

_Below is an example of how you can instruct your audience on installing and setting up your app. This template doesn't rely on any external dependencies or services._

1. Clone the repo
   ```sh
   git clone https://github.com/Bahromiddin-0256/alpha-yaproq.git
   ```
2. Create virtual environment  and activate
   ```sh
   virtualenv venv && source venv/bin/activate
   ```
3. Install PyTorch to your computer [WebSite](https://pytorch.org/)
    ```sh
    pip3 install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cpu
    ```

4. Install requirements (kerakli kutubxonalarni o'rnatib bo'lgunicha biroz vaqt olishi mumkin)
   ```sh
   pip install -r requirements.txt
   ```

5. Copy [.env.example](https://github.com/Bahromiddin-0256/alpha-yaproq/blob/main/.env.example)  to .env and change variables to yours
   ```sh
   cp .env.example .env
   ```
6. Malumotlar bazasini saqlang
    ```sh
    python manage.py makemigrations && python manage.py migrate
    ```
- Create super user
    ```sh
    python manage.py createsuperuser
    ```
- To run the bot in development run and to run the bot in production just run
    ```sh
    python manage.py runbot 
    uvicorn main.asgi:application
    ```



<!-- USAGE EXAMPLES -->
## Usage

Telegram botga kirib /start buyrug'idan so'ng sizdaquidagi komandalar chiqadi
![Alt text](image.png)


See the [open issues](https://github.com/Bahromiddin-0256/alpha-yaproq/issues) for a full list of proposed features (and known issues).


<!-- CONTRIBUTING -->
## Contributing

Contributions are what make the open source community such an amazing place to learn, inspire, and create. Any contributions you make are **greatly appreciated**.

If you have a suggestion that would make this better, please fork the repo and create a pull request. You can also simply open an issue with the tag "enhancement".
Don't forget to give the project a star! Thanks again!

1. Fork the Project
2. Create your NewUser Branch (`git checkout -b NewUser`)
3. Commit your Changes (`git commit -m 'Add some from NewUser'`)
4. Push to the Branch (`git push origin NewUser`)
5. Open a Pull Request



<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- CONTACT -->
## Contact
ALPHA team:

- 👨‍💻 [Ibragimov Bahromiddin](https://github.com/Bahromiddin-0256)

- 👨‍💻 [Mamatmusayev Jaloliddin](https://github.com/jaloliddin1006)

- 👨‍💻 [Sindarov Jo'rabek](https://github.com/jurabek004)

- 👨‍💻 [Muhammadaliyev Nodirjon](https://github.com/muhammadaliyevnodirjon)

- 👨‍💻 [Hasanov Diyorbek](https://github.com/)

Project Link: [https://github.com/Bahromiddin-0256/alpha-yaproq](https://github.com/Bahromiddin-0256/alpha-yaproq)



<!-- ACKNOWLEDGMENTS -->
## Acknowledgments

Use this space to list resources you find helpful and would like to give credit to. I've included a few of my favorites to kick things off!

* [Choose an Open Source License](https://choosealicense.com)
* [GitHub Emoji Cheat Sheet](https://www.webpagefx.com/tools/emoji-cheat-sheet)
* [Malven's Flexbox Cheatsheet](https://flexbox.malven.co/)
* [Malven's Grid Cheatsheet](https://grid.malven.co/)
* [Img Shields](https://shields.io)
* [GitHub Pages](https://pages.github.com)
* [Font Awesome](https://fontawesome.com)
* [React Icons](https://react-icons.github.io/react-icons/search)



