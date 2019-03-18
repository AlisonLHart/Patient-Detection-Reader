import  React, { Component} from 'react';
import { connect} from 'react-redux';
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
        console.log('this', this)
        const {email} = this.props;
        const {PID} = this.state;
        const {RFID} = this.state;
        const {RN} = this.state;
        //var db = firebaseApp.firestore();
        //patientRef.collection('patient-detection-reader').doc('Patient-detection').set({PID: 'pid', RFID: 'rfid'})
        patientRef.push({email, PID, RFID, RN})
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
function mapStateToProps(state) {
    const {email} = state;
    return {
        email
    }
}


export default connect(mapStateToProps, null) (AddPatient);