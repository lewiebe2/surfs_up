# 1. Import dependencies.
import datetime as dt
import pandas as pd
import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func
from flask import Flask, jsonify

# Set up database engine for Flask app.
engine = create_engine("sqlite:///hawaii.sqlite")

# Reflect database into classes.
Base = automap_base()

# Reflect the database.
Base.prepare(engine, reflect=True)

# Create variables for the classes.
Measurement = Base.classes.measurement
Station = Base.classes.station

# Create a session link from Python to database.
session = Session(engine)

# Define the Flask app.
app = Flask(__name__)

# Define the root or welcome route.
@app.route("/")
def welcome():
    return(
    '''
    Welcome to the Climate Analysis API!
    Available Routes: 
    /api/v1.0/precipitation 
    /api/v1.0/stations 
    /api/v1.0/tobs 
    /api/v1.0/temp/start/end 
    ''')

# Define the precipitation route.
@app.route("/api/v1.0/precipitation")
def precipitation():
    prev_year = dt.date(2017, 8, 23) - dt.timedelta(days=365)
    precipitation = session.query(Measurement.date, Measurement.prcp).\
      filter(Measurement.date >= prev_year).all()
    return




