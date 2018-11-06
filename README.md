# Click to Call with Flask

This is a fork of an application example implementing Click to Call using Twilio. 

At Coworker.org, we used this to support a worker-led call-in campaign. We hosted it on Heroku, so there are a few Heroku-specific files in this repo that don't exist in the original. We also added a small reporting script, `report.py`, that let us easily see how many calls were made. You can see screenshots in [docs/](https://github.com/CoworkerOrg/clicktocall-flask/blob/master/docs).

![image of main interface](https://github.com/CoworkerOrg/clicktocall-flask/blob/master/docs/main.png)

## Local development

This project is built using the [Flask](http://flask.pocoo.org/) web framework. It runs on Python 2.7+ and Python 3.4+.

To run the app locally, first clone this repository and `cd` into its directory. Then:

1. Create a new virtual environment:
    - If using vanilla [virtualenv](https://virtualenv.pypa.io/en/latest/):

        ```
        virtualenv venv
        source venv/bin/activate
        ```

    - If using [virtualenvwrapper](https://virtualenvwrapper.readthedocs.org/en/latest/):

        ```
        mkvirtualenv clicktocall-flask
        ```

1. Install the requirements:

    ```
    pip install -r requirements.txt
    ```

1. Copy the `.env.example` file to `.env`, and edit it including your credentials for the Twilio API (found at https://www.twilio.com/user/account/settings). You will also need a [Twilio Number](https://www.twilio.com/user/account/phone-numbers/incoming).
1. Run `source .env` to apply the environment variables
1. Expose your application to the wider internet using ngrok. You can click [here](#expose-the-application-to-the-wider-internet) for more details. This step is important because the application won't work as expected if you run it through localhost.

   ```bash
   $ ngrok http 5000
   ```

1. Start the development server:

    ```
    make run
    ```

Once Ngrok is running, open up your browser and go to your Ngrok URL. It will
look like this: `http://9a159ccf.ngrok.io`

That's it!

## Meta

* No warranty expressed or implied.  Software is as is. Diggity.
* [MIT License](http://www.opensource.org/licenses/mit-license.html)
* Lovingly crafted by Twilio Developer Education.
