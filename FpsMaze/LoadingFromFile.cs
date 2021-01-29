using UnityEngine;
using System.Collections;
using System.IO;
using System.Collections.Generic;
using System;

public class LoadingFromFile : MonoBehaviour
{
    public int N;
    public int K;
    public int L;
    string readFile;
    public List<string> stringList = new List<string>();
    void Awake(){
        readFile = "Assets/Resources/file.maz";
    }
    public void  ReadFile(){
        StreamReader reader = new StreamReader(readFile); 
        string text;
        int counter =0;
        do{
            text = reader.ReadLine();
            stringList.Add(text);
            counter++;
        }while(text != null);
        reader.Close();
        //Debug.Log(counter);
        string[] l = stringList[0].Split('='); 
        L = Int32.Parse(l[1]);
        string[] n = stringList[1].Split('='); 
        N = Int32.Parse(n[1]);
        string[] k = stringList[2].Split('='); 
        K = Int32.Parse(k[1]);
    }
}
