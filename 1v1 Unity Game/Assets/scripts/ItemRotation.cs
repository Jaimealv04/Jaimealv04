using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class ItemRotation : MonoBehaviour {

	// Use this for initialization
	void Start () {
		
	}
	
	// Update is called once per frame
	void Update () {
	}
	void OnTriggerEnter(Collider otro){
		if (otro.tag == "samurai"){
		//Destroy(this.gameObject);
		}

		if (otro.tag == "hamburguesa"){
		Destroy(this.gameObject);
		}
	}
}
