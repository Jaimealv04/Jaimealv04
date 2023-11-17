using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class disparador : MonoBehaviour {

	public GameObject bala;

	// Use this for initialization
	void Start () {
		
	}
	
	// Update is called once per frame
	void Update () {

		if (Input.GetKey ("f")) {
			Instantiate (bala, this.transform.position, this.transform.rotation);
		}
		
	}
}
