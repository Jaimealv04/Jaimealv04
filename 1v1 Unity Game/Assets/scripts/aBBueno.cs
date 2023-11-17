using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class aBBueno : MonoBehaviour {
	public bool derecha = true;
	// Use this for initialization
	void Start () {
		
	}
	
	// Update is called once per frame
	void Update () {
		if(Input.GetKeyDown(KeyCode.D)){
			derecha = true;
		}
		if(Input.GetKeyDown(KeyCode.A)){
			derecha = false;
		}

		if(this.transform.localEulerAngles.y <180 && derecha == false){
			this.transform.Rotate(0,5.0f,0);
		}
		if(this.transform.localEulerAngles.y > 0 && derecha == true){
			this.transform.Rotate(0,-5.0f,0);
		}
	}
}
