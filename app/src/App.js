import React, { useState, useEffect } from 'react';
import {Navbar, Button, Card, Elevation, Alignment, FormGroup, InputGroup} from '@blueprintjs/core'
import '@blueprintjs/core/lib/css/blueprint.css';

function App() {
  const [currentTime, setCurrentTime] = useState(0);

  useEffect(() => {
    fetch('/time').then(res => res.json()).then(data => {
      setCurrentTime(data.time);
    });
  }, []);

  return (
    <div className="app">
    <Navbar className="bp3-dark" >
    <Navbar.Group align={Alignment.LEFT}>
        <Navbar.Heading >FML</Navbar.Heading>
    </Navbar.Group>
    </Navbar>
    <form action = "http://localhost:5000/result" method = "POST">

    <div style={{display: 'flex', flex: 'row', width: '70%'}}>
    <Card interactive={true} elevation={Elevation.TWO} style={{margin:30, width: '100%'}}>
    <h2><a>if</a></h2>
    <RuleForm/>
</Card>
<Card interactive={true} elevation={Elevation.TWO} style={{margin:30, width: '100%'}}>
    <h2><a>...then</a></h2>
    <TradeForm/>
</Card>

    </div>
    <div style={{width: '70%'}}>
    <Card interactive={true} elevation={Elevation.TWO} style={{margin:30}}>
    <h2><a>backtest</a></h2>
    <TestForm/>
    
</Card>

</div>
</form>
    </div>
  );
}

class TestForm extends React.Component{
  constructor(props) {
    super(props);
  }
  render() {
    return (
      <div>
      <div style={{display: 'flex', flex:"row"}}>
                  <FormGroup
                  label="start_date"
                  labelFor="start-input"
                  style={{marginRight:10}}>
                  <InputGroup id="start-input" name="start-date" placeholder="06-02-2000"/>
                </FormGroup>

                <FormGroup
                  label="end_date"
                  labelFor="end-input" style={{marginRight:10}}>
                    <InputGroup id="end-input" name="end-date" placeholder="05-04-2020" />
                </FormGroup>

     </div>
                <Button icon="dollar" type="submit" value="submit"/>
     </div>
    );
  }
}

class TradeForm extends React.Component{
  constructor(props) {
    super(props);
  }
  render() {
    return (
      <div style={{display: 'flex', flex:"row"}}>
                  <FormGroup
                  label="asset"
                  labelFor="asset-input"
                  style={{marginRight:10}}>
                  <InputGroup id="asset-input" 
                  name="asset" placeholder="AAPL" />
                </FormGroup>

                <FormGroup
                  label="quantity"
                  labelFor="quantity-input" style={{marginRight:10}}>
                    <InputGroup id="quantity-input" 
                  name="quantity" placeholder="10" />
                </FormGroup>


                <FormGroup
                  label="action"
                  labelFor="action-input">
                    <InputGroup id="action-input" 
                  name="action" placeholder="buy" />
                </FormGroup>
     </div>
    );
  }
}


class RuleForm extends React.Component{
  constructor(props) {
    super(props);
    this.state = {value: [], count: 1}; //initial you'll have one form
  }

  addMore(){
    this.setState({count: this.state.count+1})//on click add more forms
  }

  displayForm(){
     let forms = [];
     for(let i = 0; i < this.state.count; i++){
               forms.push(
               <div key={i} style={{display: 'flex', flex:"row"}}>
                  <FormGroup
                  label="key"
                  labelFor="key-input"
                  style={{marginRight:10}}>
                  <InputGroup id="key-input" 
                  name={"key"+i} placeholder="transformation" />
                </FormGroup>

                <FormGroup
                  label="value"
                  labelFor="value-input">
                    <InputGroup id="value-input" 
                  name={"value"+i} placeholder="greater than" />
                </FormGroup>
                </div>
            )
     }
     return forms || null;
  }

  render() {
    return (
      <div >
          {this.displayForm()}        
          <Button icon='add' onClick={this.addMore.bind(this)}/>
      </div>
    );
  }
}


export default App;
