import React, { useState } from "react";
import LoadingBar from "react-top-loading-bar";

<div>
  <LoadingBar color="#f11946" progress={10} />
</div>;

async updateNews(){
    this.prop.setProgress(10);
    const url='http://127.0.0.1:8000/main';
    this.setState({loading:true});
    let data = await fetch(url);
    this.props.setProgress(30);
    let parsedData=await data.json()
    this.setState({
        articles:parsedData.articles,
        totalResults:parsedData.totalResults,
        loading:false,
    })
    this.props.setProgress(30);
}

export default App;
