using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class movHambur : MonoBehaviour {

	public bool derecha;
	// Use this for initialization
	void Start () {
		derecha = false;

	}
	void Update () {
		if(Input.GetKey(KeyCode.Keypad3)){
			derecha = true;
		}
		if(Input.GetKey(KeyCode.Keypad1)){
			derecha = false;
		}

		Debug.Log (this.transform.localEulerAngles.y);
		if(this.transform.eulerAngles.y >= 180.0f &&  this.transform.eulerAngles.y <= 360.0f){
			Debug.Log ("puedo Girar");
			if(derecha == false &&  this.transform.eulerAngles.y <= 330.0f){
				//derecha = false;
				Debug.Log("q");
				this.transform.eulerAngles += new Vector3 (0,10,0);
			}

			if(derecha == true &&  this.transform.eulerAngles.y >= 210.0f){
				this.transform.eulerAngles -= new Vector3 (0,10,0);

			}
		}
	}
}

