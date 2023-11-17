using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class ParticulasMELE : MonoBehaviour {
public GameObject chispas;
	// Use this for initialization
	void Start () {
		
	}
	
	// Update is called once per frame
	void Update () {
		
	}

	void OnTriggerEnter(Collider otro){
		Instantiate(chispas,this.transform.position, this.transform.rotation);
	}
}
