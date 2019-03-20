import React, {Component} from 'react';

class PatientItem extends Component {
    render() {
        //console.log('this.props.patient', this.props.patients)
        const {PID, RN, Risk} = this.props.patient;
        return(
            <div style= {{margin: '5px'}}>
                <span>Patient ID: <strong>{PID}</strong></span>
                <span> Room Number <strong>{RN}</strong></span>
                <span> Risk Level: <strong>{Risk}</strong></span>
            </div>
        )
    }
}

export default PatientItem;