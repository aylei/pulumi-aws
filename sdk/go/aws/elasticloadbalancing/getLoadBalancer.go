// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

package elasticloadbalancing

import (
	"github.com/pulumi/pulumi/sdk/go/pulumi"
)

// Provides information about a "classic" Elastic Load Balancer (ELB).
// See [LB Data Source](/docs/providers/aws/d/lb.html) if you are looking for "v2"
// Application Load Balancer (ALB) or Network Load Balancer (NLB).
// 
// This data source can prove useful when a module accepts an LB as an input
// variable and needs to, for example, determine the security groups associated
// with it, etc.
func LookupLoadBalancer(ctx *pulumi.Context, args *GetLoadBalancerArgs) (*GetLoadBalancerResult, error) {
	inputs := make(map[string]interface{})
	if args != nil {
		inputs["name"] = args.Name
		inputs["tags"] = args.Tags
	}
	outputs, err := ctx.Invoke("aws:elasticloadbalancing/getLoadBalancer:getLoadBalancer", inputs)
	if err != nil {
		return nil, err
	}
	return &GetLoadBalancerResult{
		AccessLogs: outputs["accessLogs"],
	}
		AvailabilityZones: outputs["availabilityZones"],
	}
		ConnectionDraining: outputs["connectionDraining"],
	}
		ConnectionDrainingTimeout: outputs["connectionDrainingTimeout"],
	}
		CrossZoneLoadBalancing: outputs["crossZoneLoadBalancing"],
	}
		DnsName: outputs["dnsName"],
	}
		HealthCheck: outputs["healthCheck"],
	}
		IdleTimeout: outputs["idleTimeout"],
	}
		Instances: outputs["instances"],
	}
		Internal: outputs["internal"],
	}
		Listeners: outputs["listeners"],
	}
		SecurityGroups: outputs["securityGroups"],
	}
		SourceSecurityGroup: outputs["sourceSecurityGroup"],
	}
		SourceSecurityGroupId: outputs["sourceSecurityGroupId"],
	}
		Subnets: outputs["subnets"],
	}
		Tags: outputs["tags"],
	}
		ZoneId: outputs["zoneId"],
	}
	}, nil
}

// A collection of arguments for invoking getLoadBalancer.
type GetLoadBalancerArgs struct {
	// The unique name of the load balancer.
	Name interface{}
	Tags interface{}
}

// A collection of values returned by getLoadBalancer.
type GetLoadBalancerResult struct {
	AccessLogs interface{}
	AvailabilityZones interface{}
	ConnectionDraining interface{}
	ConnectionDrainingTimeout interface{}
	CrossZoneLoadBalancing interface{}
	DnsName interface{}
	HealthCheck interface{}
	IdleTimeout interface{}
	Instances interface{}
	Internal interface{}
	Listeners interface{}
	SecurityGroups interface{}
	SourceSecurityGroup interface{}
	SourceSecurityGroupId interface{}
	Subnets interface{}
	Tags interface{}
	ZoneId interface{}
}
