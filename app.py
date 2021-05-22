# Import Libraries
import numpy as np
import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func
from flask import Flask, jsonify, render_template


# Database Setup
engine = create_engine("sqlite:///Resources/hawaii.sqlite")

# Reflect the hawaii database into a new model
Base = automap_base()

# Reflect the tables
Base.prepare(engine, reflect=True)

# Save references to the table
Measurement = Base.classes.measurement
Station = Base.classes.station

# Flask Setup
app = Flask(__name__)
app.config['JSON_SORT_KEYS'] = False

# Flask Routes

# 1. The Home Page
@app.route("/")
def welcome():
    """Welcome to Climate App"""
    return render_template("welcome.html")
    #     f"<pre><H2><strong>Welcome to Climate App </strong></h2><br></pre>"
    #     f"<img src='{{ url_for('static', filename='surfs-up.png') }}' />"
    #     f"<pre><h3><strong>Here are the available Routes:</h4></strong><br>"
    #     f"<br>"
    #     f"<pre>/api/v1.0/precipitation       -   Returns a JSON representation of the 23/08/2016 - 23/08/2017 precipitation analysis</pre><br/>"
    #     f"<pre>/api/v1.0/stations            -   Returns a data on all stations in JSON format</pre><br>"       
    #     f"<pre>/api/v1.0/tobs                -   Returns a JSON list of all temperature observations from 23/08/2016 - 23/08/2017</pre><br>"
    #     f"<pre>/api/v1.0/                    -   Enter a start date +/- end date in format '/api/v1.0/YYYY-MM-DD/YYYY-MM-DD' to view the min, max and avg</pre>"
    #     f"<pre>                                  temps for each day in the range. If end date empty all dates greater than start date will be used</pre>"
    #     f"<pre>                                  The database spans dates 1/1/2010 to 23/08/2017</pre>" 
    # )

# 2. The Precipitation Route
@app.route("/api/v1.0/precipitation")
def precipitation():
    # Create our session from Python to the DB
    session = Session(engine)

    # Query the precipitation data 
    result = session.query(Measurement.date, Measurement.prcp).\
    filter(Measurement.date >= '2016-08-23').all()

    session.close()

    # Convert the results to a dictionary with data as key and prcp as value 
    prcp_data = []
    for date, prcp in result:
        dict = {}
        dict[date] = prcp
        prcp_data.append(dict)

    return jsonify(prcp_data)

# 3. The Stations Route
@app.route("/api/v1.0/stations")
def stations():
    # Create session from Python to the DB
    session = Session(engine)

    # Query the station data 
    result = session.query(Station.id, Station.name, Station.latitude, Station.longitude, 
                            Station.elevation).all()

    session.close()

    # Convert the results to a dictionary
    station_data = []
    for id, name, lat, long, elev in result:
        dict = {}
        dict['ID'] = id
        dict['Name'] = name
        dict['Lat'] = lat
        dict['Lon'] = long
        dict['Elevation'] = elev    
        station_data.append(dict)

    return jsonify(station_data)

# 4. The Temperature Observations Route
@app.route("/api/v1.0/tobs")
def tobs():
    # Create session from Python to the DB
    session = Session(engine)

    # Query the tobs data 
    sel = [Station.station, Station.name, Measurement.station, Measurement.date, Measurement.tobs]
    result = session.query(*sel).filter(Station.station == Measurement.station).filter(
                           Station.id == 7).filter(Measurement.date >= '2016-08-23').all()

    session.close()

    # Convert the results to a dictionary
    tobs_data = []
    for station, name, station2, date, tobs in result:
        dict = {}
        dict['Date'] = date
        dict['Name'] = name
        dict['Station'] = station        
        dict['TOBS'] = tobs
        tobs_data.append(dict)

    return jsonify(tobs_data)

# 5. The Temp by Date Range Router
@app.route("/api/v1.0/<start_date>/<end_date>")
@app.route("/api/v1.0/<start_date>")
def temp_by_date(start_date, end_date=None):
    # Create session from Python to the DB
    session = Session(engine)

    if end_date == None:
        # Query the tobs data 
        result = session.query(Measurement.date, func.min(Measurement.tobs), func.max(Measurement.tobs), 
                               func.round(func.avg(Measurement.tobs),2)).filter(
                               Measurement.date >= start_date).group_by(Measurement.date).all()
        session.close()

        # Convert the results to a dictionary
        date_temp_data = []
        for date, min, max, avg, in result:
            dict = {}
            dict['Date'] = date
            dict['Min'] = min
            dict['Max'] = max
            dict['Avg'] = avg
            date_temp_data.append(dict)

        return jsonify(date_temp_data)

    else:        
        # Query the tobs data 
        result = session.query(Measurement.date, func.min(Measurement.tobs), 
                               func.max(Measurement.tobs), func.round(func.avg(Measurement.tobs),2)).filter(
                               (Measurement.date >= start_date) & (Measurement.date <= end_date)).group_by(Measurement.date).all()
        session.close()

        # Convert the results to a dictionary
        date_temp_data = []
        for date, min, max, avg, in result:
            dict = {}
            dict['Date'] = date
            dict['Min'] = min
            dict['Max'] = max
            dict['Avg'] = avg
            date_temp_data.append(dict)

        return jsonify(date_temp_data)




if __name__ == '__main__':
    app.run(debug=True)
