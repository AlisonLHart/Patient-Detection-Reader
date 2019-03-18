import  React, { Component} from 'react';
import {patientRef, firebaseApp} from '../firebase';

class AddPatient extends Component{
    constructor(props){
        super(props);
        this.state = {
            PID: '',
            RFID: '',
            RN: ''
        }
    }

    addPatient(){
        console.log('this.state', this.state)
        //var db = firebaseApp.firestore();
        //patientRef.collection('patient-detection-reader').doc('Patient-detection').set({PID: 'pid', RFID: 'rfid'})
        patientRef.push({Patient_Info: this.state})
    }
    render () {
        return (
            <div className="form-inline">
            <div className="form-group">
            <input 
                type="text"
                placeholder="Patient ID"
                className="form-control"
                style={{marginRight: '5px'}}
                onChange={event => this.setState({PID: event.target.value})}
                />
                <input 
                type="text"
                placeholder="Add an RFID tag"
                className="form-control"
                style={{marginRight: '5px'}}
                onChange={event => this.setState({RFID: event.target.value})}
                />
                <input 
                type="text"
                placeholder="Patient Room Number"
                className="form-control"
                style={{marginRight: '5px'}}
                onChange={event => this.setState({RN: event.target.value})}
                />
                <button
                    className="btn btn-success"
                    type= "button"
                    onClick={() => this.addPatient()}
                >Submit</button>
            </div>

            </div>
        )
    }

}

export default AddPatient;