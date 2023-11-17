using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class ROTACIONDEMELE : MonoBehaviour {

public float velROT;
	// Use this for initialization
	void Start () {
		velROT = -20;
	}
	
	// Update is called once per frame
	void Update () {
		if (Input.GetKey("g")){
				this.transform.Rotate(0,0,velROT);
		}
	}
}
