"use client";

import { Slider } from "antd";
import { useState } from "react";

export default function Home() {
  const [value, setValue] = useState(50);

  return (
    <main className="flex flex-col gap-6 items-center justify-center min-h-screen">
      <h1 className="text-2xl font-bold">Ant Design Slider Example</h1>
      
      <Slider 
        min={0} 
        max={100} 
        value={value} 
        onChange={(val) => setValue(val)} 
        style={{ width: 300 }} 
      />
      
      <p className="text-lg">Volume: {value}%</p>
    </main>
  );
}
