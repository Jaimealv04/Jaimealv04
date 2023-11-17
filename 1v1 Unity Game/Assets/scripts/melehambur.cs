using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class melehambur : MonoBehaviour {

	
	public float VelROT;
	// Use this for initialization
	void Start () {
		VelROT = -20;
	}
	
	// Update is called once per frame
	void Update () {
		if (Input.GetKey(KeyCode.Keypad2)){
				this.transform.Rotate(0,0,VelROT);
		}
	}
}