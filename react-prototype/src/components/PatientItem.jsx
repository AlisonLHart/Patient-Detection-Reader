import React, {Component} from 'react';

class PatientItem extends Component {
    render() {
        //console.log('this.props.patient', this.props.patients)
        const {PID, RN, Risk} = this.props.patient;
        return(
            <div style= {{margin: '5px'}}>
                <span>{PID}</span>
                <span>{RN}</span>
                <span>{Risk}</span>
            </div>
        )
    }
}

export default PatientItem;