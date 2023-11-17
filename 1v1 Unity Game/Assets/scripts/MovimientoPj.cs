using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class MovimientoPj : MonoBehaviour {
	
	public GameObject anim;
		//giro del muñeco
	public bool derecha;
	// Use this for initialization
	void Start () {
		derecha = false;
		anim = GameObject.Find("Personaje_Unity_rigging(1)");
		anim.GetComponent<Animator>().SetBool("corriendo", false);
	}
	void Update () {
		if(Input.GetKeyDown("d")){
			derecha = true;
			anim.GetComponent<Animator>().SetBool("corriendo", true);
		}
		if(Input.GetKeyDown("a")){
			derecha = false;
			anim.GetComponent<Animator>().SetBool("corriendo", true);
		}
		if(Input.GetKeyUp("d")||Input.GetKeyUp("a")){
			anim.GetComponent<Animator>().SetBool("corriendo", false);
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
