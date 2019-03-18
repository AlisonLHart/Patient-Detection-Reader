import React, {Component} from 'react';
import {patientRef} from '../firebase'

class PatientList extends Component{
    componentDidMount() {
        patientRef.on('value', snap => {
            snap.forEach(patient => {
                let patientObject = patient.val();
                console.log('patientObject', patientObject)
            })
        })
    }
    render(){
        return (
            <div>PatientList</div>
        )
    }

}

export default PatientList