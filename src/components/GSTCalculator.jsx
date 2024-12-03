
import React, { useState } from 'react';
import axios from 'axios';
import './gstcalculator.css';  

const GSTCalculator = () => {
  const [amount, setAmount] = useState('');
  const [gstRate, setGstRate] = useState('');
  const [type, setType] = useState('');
  const [gst, setGst] = useState(null);
  const [total, setTotal] = useState(null);
  const [error, setError] = useState('');

  const handleCalculateGST = async () => {
    try {
      const response = await axios.post('http://127.0.0.1:8000/api/gst/calculate/', {
        amount: amount,
        gst_rate: gstRate,
        type: type
      });

      setGst(response.data.gst);
      setTotal(response.data.total);
      setError('');
    } catch (err) {
      setError('Error: ' + err.response?.data?.error || 'An error occurred');
      setGst(null);
      setTotal(null);
    }
  
  };
   
  return (
    <div className='div'>
      <h1>GST CALCULATOR</h1>
      
      <input
        type="number"
        placeholder="Enter Amount"
        value={amount}
        onChange={(e) => setAmount(e.target.value)}
      />

      <select name="" type="number" className="input">
        <option value=""></option>
        <option value=""> 5% </option>
        <option value=""> 12 % </option>
        <option value=""> 18 % </option>
        <option value=""> 28 % </option>
        value={gstRate}
        onChange={(e) => setGstRate(e.target.value)}
      </select>
   
      

      <select name="" className="select">
        <option value=""></option>
        <option value="">Exclusive</option>
        <option value="">Inclusive</option>
        value={type}
        onChange={(e) => setType(e.target.value)}
      </select>
    

      <button onClick={handleCalculateGST}>Calculate</button>

      {error && <p className="error">{error}</p>}

      {gst !== null && total !== null && (
        <div>
          <p className="success">GST: {gst}</p>
          <p className="success">Total: {total}</p>
        </div>
      )}
    </div>
  );
};

export default GSTCalculator;

