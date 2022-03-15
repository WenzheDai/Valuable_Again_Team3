


<!-- PROJECT LOGO -->
<br />
<div align="center">
  <a href="https://github.com/github_username/repo_name">
    <img src="https://upload.wikimedia.org/wikipedia/commons/4/46/Glasgow_Coat_of_Arms.png" alt="Logo" width="400" height="400">
  </a>

<h1 align="center">VALUABLE AGAIN</h1><h3 align="center"></h3><h3 align="center">An Online Merchandise System For The City Of Glasgow</h3>

  <p align="center">
    <br />
  </p>
</div>



<!-- TABLE OF CONTENTS -->
<details>
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
      <ul>
        <li><a href="#built-with">Built With</a></li>
      </ul>
    </li>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#prerequisites">Prerequisites</a></li>
        <li><a href="#installation">Installation</a></li>
      </ul>
    </li>
    <li><a href="#usage">Usage</a></li>
    <li><a href="#roadmap">Roadmap</a></li>
    <li><a href="#contributing">Contributing</a></li>
    <li><a href="#license">License</a></li>
    <li><a href="#contact">Contact</a></li>
    <li><a href="#acknowledgments">Acknowledgments</a></li>
  </ol>
</details>



<!-- ABOUT THE PROJECT -->
## About The Project


The objective of our application is to provide a web platform for information sharing, discussion and communication for people who want to buy second-hand items and sell second-hand items in Glasgow.
On this platform, everyone can browse and retrieve the products they want.
Users can create their own account and post second-hand items they want to sell, as well as pre-order the items they want and get the contact details and general location of the seller.
Sellers can view the pre-order information for their items, as well as update their item information and confirm when the transaction is completed, and the item is automatically taken off the shelf.


### Built With

* [django 2.2.5](https://www.djangoproject.com)
* [Python 3.7.5](https://www.python.org)
* [Bootstrap](https://getbootstrap.com)



<!-- GETTING STARTED -->
## Getting Started

This is an example of how you may give instructions on setting up your project locally.
To get a local copy up and running follow these simple example steps.

### Prerequisites

Install Anaconda for vitual enviroments. 


### Installation

1. Create the workspace folder, clone or pull the source files:
   ```
   Git clone https://github.com/WenzheDai/Valuable_Again_Team3.git
   ```
2. Using pip to set eviroment. requirements.txt that can be used to install the relevant packages within a newly-created virtual environment
   ```
   pip install –r requirements.txt
   ```
3. Set up the eviroment if the prerequisites requirements.txt isn't executed.
   ```conda 
   create -n Valuable_Again_Team3 python=3.7.5
   ```
   ```
   conda activate Valuable_Again_Team3
   ```
   ```
   conda install django==2.2.5
   ```
   ```
   conda install pillow
   ```

3. In Valuable_Again_Team3 directory, again if the prerequisites requirements.txt isn't executed, do the following:
   ```
   pip install django-haystack
   pip install whoosh
   ```
4. Delete cache files or database files if there are any:
   ```
   find . | grep -E "(__pycache__|\.pyc|\.pyo$)" | xargs rm -rf
   ```
   ```
   rm db.sqlite3
   ```
5. Run database migrations:
   ```
   python manage.py makemigrations
   python manage.py migrate
   python population_script.py
   python manage.py rebuild_index
   ```
6. Run the server:
   ```
   python manage.py runserver
   ```

<!-- USAGE EXAMPLES -->
## Usage

The functions of the system include the following:
1. Users can register, log in and log out of their accounts.
2. Users must be registered and logged in to reserve and post products.
3. Users can search for products by category, name and description information.
4. Users can only update the information of the products they have posted.
5. The user can view the location and contact details of the seller of the item booked.
6. Everyone can view the details of all products.
7. Sellers and buyers can rate and comment on their integrity after the transaction is completed. And displayed on the personal home page.
8. Administrators can view details of all users and products as well as transaction history. 

## Contributers

- Mr Dai
- Mr Ma
- Mrs He
- Mr Yang
- Mr Wang
