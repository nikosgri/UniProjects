using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class FPSPlayer : MonoBehaviour
{
     public GameObject hand;
     private LoadingFromFile LFF;
    // Start is called before the first frame update
    void Awake(){
        LFF = GetComponent<LoadingFromFile>();
    }
    void Start()
    {
        //FindARandomEmptyPlace();
        //hand = GameObject.Find("FPSPlayer");
        //hand.transform.position = new Vector3(0,4,0);
    }

    // Update is called once per frame
    void FindARandomEmptyPlace(){
        int L = LFF.L;
        int N = LFF.N;
        List<int> intList = new List<int>();
        int counter=0;
        List<string> stringList = new List<string>();
        stringList.AddRange(LFF.stringList);
        string[] cubes;
        int x=0,z=0;
        for(int j=4;j<N+4;j++){
            cubes = stringList[j].Split(' ');
            for(int i=0;i<cubes.Length;i++){
                if(cubes[i].Equals("B")||cubes[i].Equals("G")||cubes[i].Equals("R")||cubes[i].Equals("T1")||cubes[i].Equals("T2")||cubes[i].Equals("T3")||cubes[i].Equals("E")){
                    if(cubes[i].Equals("E")){
                        intList.Add(x);
                        intList.Add(z);
                        Debug.Log(x); 
                        Debug.Log(z);
                        Debug.Log(cubes[i]);  
                        x++; 
                        counter=counter+2;
                    }
                    else{
                        x++;
                    }
                }
            }
            x=0;
            z++;
        }
    }
}
