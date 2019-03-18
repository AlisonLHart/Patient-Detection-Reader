import React, {Component} from 'react';
import { connect } from 'react-redux';
import {patientRef} from '../firebase';
import {setPatients} from  '../actions';

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
            console.log('patients', patients);
            this.props.setPatients(patients);
        })
    }
    render(){
        console.log('this.props.patients', this.props.patients);
        return (
            <div>
            {
                this.props.patients.map(patient => {
                    return (
                        <div>{patient.PID}</div>
                    )
                })
            }
            </div>
        )
    }

}

function mapStateToProps(state){
    const {patients} = state;
    return{
        patients
    }
}

export default connect(mapStateToProps,{setPatients})(PatientList);