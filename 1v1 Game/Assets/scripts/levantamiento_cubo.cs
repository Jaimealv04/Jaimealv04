using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class levantamiento_cubo : MonoBehaviour {

	// Update is called once per frame
	void Update () {
		

		if (this.transform.position.y >= 6){
			this.transform.position = new Vector3 (8.0f,6.00f,20.0f);
		}else{
			this.transform.Translate(0,0.2f, 0);
		}
	}

	
}
