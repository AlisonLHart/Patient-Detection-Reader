import  React, { Component} from 'react';
import { connect} from 'react-redux';
import {patientRef} from '../firebase';
//import {ToggleButton,ToggleButtonGroup} from 'react-bootstrap'
//import Switch from "react-switch";

class AddPatient extends Component{
    constructor(props){
        super(props);
        this.state = {
            PID: '',
            RFID: '',
            RN: '',
            emailTwo: '',
            Risk: 'NO RFID',
        }

    }

    addPatient(){
        console.log('this', this)
        const {email} = this.props.user;
        const {PID} = this.state;
        const {RFID} = this.state;
        const {RN} = this.state;
        const {emailTwo} = this.state;
        const {Risk} = this.state;
        //var db = firebaseApp.firestore();
        //patientRef.collection('patient-detection-reader').doc('Patient-detection').set({PID: 'pid', RFID: 'rfid'})
        patientRef.push({email, PID, RFID, RN, emailTwo, Risk})
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
    const {user} = state;
    return {
        user
    }
}


export default connect(mapStateToProps, null) (AddPatient);