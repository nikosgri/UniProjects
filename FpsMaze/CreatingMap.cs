using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class CreatingMap : MonoBehaviour
{
    private LoadingFromFile LFF;
    private List<int> intList;
    MeshRenderer myRenderer;
    public GameObject hand;
    int counter;
    void Awake(){
        LFF = GetComponent<LoadingFromFile>();
        intList = new List<int>();
        counter=0;
    }
    void Start()
    {
        LFF.ReadFile();
        CreateGround();
        CreateBounds();
        CreateLevels();
        Spawn();
    }
    void CreateGround(){
        int N = LFF.N;
        int L = LFF.L;
        GameObject Ground = GameObject.CreatePrimitive(PrimitiveType.Plane);
        Ground.transform.position = new Vector3(N/2f,-0.5f,N/2f);
        Ground.transform.localScale = new Vector3(N/8,1,N/8);
        var planeRenderer = Ground.GetComponent<Renderer>();
    }
    void CreateBounds(){
        int N = LFF.N;
        int L = LFF.L;
        GameObject leftWall = GameObject.CreatePrimitive(PrimitiveType.Cube);
        leftWall.transform.position = new Vector3(-1f,1.5f,(N-1)/2f);
        leftWall.transform.localScale = new Vector3(1,L,N);
        var leftWallRenderer = leftWall.GetComponent<Renderer>();
        leftWallRenderer.enabled=false;

        GameObject rightWall = GameObject.CreatePrimitive(PrimitiveType.Cube);
        rightWall.transform.position = new Vector3(N,1.5f,(N-1)/2f);
        rightWall.transform.localScale = new Vector3(1,L,N);
        var rightWallRenderer = rightWall.GetComponent<Renderer>();
        rightWallRenderer.enabled=false;

        GameObject downWall = GameObject.CreatePrimitive(PrimitiveType.Cube);
        downWall.transform.position = new Vector3((N-1)/2f,1.5f,-1f);
        downWall.transform.localScale = new Vector3(1,L,N);
        downWall.transform.Rotate(0,90,0);
        var downWallplaneRenderer = downWall.GetComponent<Renderer>();
        downWallplaneRenderer.enabled=false;

        GameObject upWall = GameObject.CreatePrimitive(PrimitiveType.Cube);
        upWall.transform.position = new Vector3((N-1)/2f,1.5f,N);
        upWall.transform.localScale = new Vector3(1,L,N);
        upWall.transform.Rotate(0,90,0);
        var upWallplaneRenderer = upWall.GetComponent<Renderer>();
        upWallplaneRenderer.enabled=false;
    }
    void CreateLevels(){
        int N = LFF.N;
        int L = LFF.L;
        List<string> stringList = new List<string>();
        stringList.AddRange(LFF.stringList);
        string[] cubes;
        int x=0,y=0,z=0;
        for(int j=4;j<N*L+L;j++){
            cubes = stringList[j].Split(' ');
            for(int i=0;i<cubes.Length;i++){
                if(cubes[i].Equals("B")||cubes[i].Equals("G")||cubes[i].Equals("R")||cubes[i].Equals("T1")||cubes[i].Equals("T2")||cubes[i].Equals("T3")||cubes[i].Equals("E")){
                    if(cubes[i].Equals("E")){
                        
                        if(y==0){
                            intList.Add(x);
                            intList.Add(z);
                            counter++;
                        }
                        x++;
                    }
                    else{
                        CreateCubes(x,y,z,cubes[i]);
                        x++;
                    }
                }
            }
            x=0;
            z++;
            if(z==16){
                y++;
                z=0;
            }
        }
    }
    void CreateCubes(float x ,float y , float z , string c){
        GameObject cube = GameObject.CreatePrimitive (PrimitiveType.Cube);
        cube.transform.position = new Vector3(x,y,z);
        var cubeRenderer = cube.GetComponent<Renderer>();
        if(c.Equals("R")){
            cubeRenderer.material.SetColor("_Color",Color.red);
        }
        else if(c.Equals("G")){
            cubeRenderer.material.SetColor("_Color",Color.green);
        }
        else if(c.Equals("B")){
            cubeRenderer.material.SetColor("_Color",Color.blue);
        }
        else if(c.Equals("T1")){
            Texture2D tex = Resources.Load("T1") as Texture2D;
            cubeRenderer.material.mainTexture=tex;
        }
        else if(c.Equals("T2")){
            Texture2D tex = Resources.Load("T2") as Texture2D;
            cubeRenderer.material.mainTexture=tex;
        }
        else if(c.Equals("T3")){
            Texture2D tex = Resources.Load("T3") as Texture2D;
            cubeRenderer.material.mainTexture=tex;
        }
    }
    void Spawn(){
        int rand = Random.Range(1,counter);
        hand = GameObject.Find("FPSPlayer");
        int x = rand*2;
        int z = rand*2 +1;
        hand.transform.position = new Vector3(intList[x],0,intList[z]);
    }
}
