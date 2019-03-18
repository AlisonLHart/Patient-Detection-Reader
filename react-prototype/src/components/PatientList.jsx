import React, {Component} from 'react';
import {patientRef} from '../firebase'

class PatientList extends Component{
    componentDidMount() {
        patientRef.on('value', snap => {
            let patients = [];
            snap.forEach(patient => {
                //let patientObject = patient.val();
                const {email, PID, RFID, RN} = patient.val();
                //console.log('patientObject', patientObject)
                patients.push({email, PID, RFID, RN});
            })
            console.log('patients', patients)
        })
    }
    render(){
        return (
            <div>PatientList</div>
        )
    }

}

export default PatientList